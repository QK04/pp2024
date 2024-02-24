import math
import curses
import numpy as np

class Student:
    def __init__ (self, student_id, student_name, DoB):
        self.student_id = student_id            
        self.student_name = student_name
        self.DoB = DoB
        self.marks = []
    
    def add_mark(self, mark):
        self.marks.append(mark)
    
class Course:
    def __init__ (self, course_id, course_name, credits):
        self.course_name = course_name
        self.course_id = course_id    
        self.credits = credits

class Mark:
    def __init__ (self, student, course, mark):
        self.student = student
        self.course = course    
        self.mark = mark


# Ask how many number of student and take student information      
class StudentManager:
    Student_list = []

    def students_information(cls):
        s = int(input("Enter Number of Students: "))
        if s <= 0:
            print("Error")
            return

        for i in range (1,s + 1):

            student_id = str(input("\nEnter Student %d ID: " %i))
            for student in StudentManager.Student_list:
                if student.student_id == student_id:
                    print("Already exist")
                    return      
                
            student_name = str(input("Enter Student %d Name: " %i))
            DoB = str(input("Enter Student %d DoB: " %i))
            cls.Student_list.append(Student(student_id, student_name, DoB))

# Display list students
    def list_students(cls):
        print("\nList Students ")
        num = 1
        for student in cls.Student_list:
            print(f"Student {num}. ID: {student.student_id}, Name: {student.student_name}, Dob: {student.DoB}")
            num = num + 1


# Ask how many number of course and take course information
class CourseManager:
    Course_list = []

    def courses_information(cls):
        c = int(input("\nEnter Number of Courses: "))
        if c <= 0:
            print("Error")
            return

        for i in range (1,c + 1):
            course_id = str(input("\nEnter Course %d ID: " %i))
            for course in CourseManager.Course_list:
                if course.course_id == course_id:
                    print("Already exist")
                    return
            course_name = str(input("Enter Couse %d Name: " %i))
            credits = int(input("Enter Credits for Course %d: " %i))
            cls.Course_list.append(Course(course_id, course_name, credits))

    # Display list courses
    def list_courses(cls):
        print("\nList Courses ")
        num = 1
        for course in cls.Course_list:
            print(f"Course {num}. ID: {course.course_id}, Name: {course.course_name}, Credits: {course.credits}")
            num = num + 1

# Select a course, input marks for student in this course
class MarkManager:
    Mark_list = []

    def mark_information(cls):
        CourseManager.list_courses(CourseManager)
        course_name = str(input("Enter Course Name: "))
        if course_name not in [course.course_name for course in CourseManager.Course_list]:
            print("Error")
            return    
        
        StudentManager.list_students(StudentManager)
        student_name = str(input("Enter Student Name: "))
        if student_name not in [student.student_name for student in StudentManager.Student_list]:        
            print("Error")
            return
        
        course = next(course for course in CourseManager.Course_list if course.course_name == course_name)
        student = next(student for student in StudentManager.Student_list if student.student_name == student_name)
        
        mark = float(input(f"Input Mark for {student_name} in {course_name}: "))
        round_down = math.floor(mark*10)/10
        cls.Mark_list.append(Mark(student, course, round_down))
        student.marks.append(Mark(student, course, round_down))

    # Display list marks
    def list_mark (cls):
        if not cls.Mark_list:
            print("No marks available.")
            return        
         
        print("List of Marks:")
        for mark in cls.Mark_list:
            student_name = mark.student.student_name
            course_name = mark.course.course_name
            print(f"Course: {course_name}, Student: {student_name}, Mark: {mark.mark}")


class GPA:
    def calculate_gpa(student):
        if not student.marks:
            return 0
        
        credits = np.array([mark.course.credits for mark in student.marks])
        marks = np.array([mark.mark for mark in student.marks])
        gpa = math.floor((np.sum(credits*marks) / np.sum(credits))*10)/10
        return gpa
    
    def sorting(Student_list):
        Student_list = sorted(Student_list, key=lambda student: GPA.calculate_gpa(student), reverse=True)
        return Student_list
    

# Main function:  Student Mark Management

def main(stdscr):
    
    stdscr.clear()
    stdscr.addstr(1, 2, "Welcome to Student Mark Management", curses.A_BOLD)
    stdscr.addstr(3, 2, "1. Input student information: id, name, DoB", curses.A_UNDERLINE)
    stdscr.addstr(4, 2, "2. Input course information: id, name", curses.A_UNDERLINE)
    stdscr.addstr(5, 2, "3. List students", curses.A_UNDERLINE)
    stdscr.addstr(6, 2, "4. List courses", curses.A_UNDERLINE)
    stdscr.addstr(7, 2, "5. Select a course, input marks for student", curses.A_UNDERLINE)
    stdscr.addstr(8, 4, "in this course", curses.A_UNDERLINE)  # Adjusted for longer string
    stdscr.addstr(9, 2, "6. Show student marks for a given course", curses.A_UNDERLINE)
    stdscr.addstr(10, 2, "7. Sorting students by GPA", curses.A_UNDERLINE)
    stdscr.addstr(11, 2, "8. Exit\n", curses.A_UNDERLINE)
    stdscr.refresh()

    stdscr.keypad(True)

    while True:
        choice = stdscr.getch() 

        if choice == ord('1'):
            StudentManager.students_information(StudentManager)
        elif choice == ord('2'):
            CourseManager.courses_information(CourseManager)
        elif choice == ord('3'):
            StudentManager.list_students(StudentManager)
        elif choice == ord('4'):
            CourseManager.list_courses(CourseManager)
        elif choice == ord('5'):
            MarkManager.mark_information(MarkManager)  
        elif choice == ord('6'):
            MarkManager.list_mark(MarkManager) 
        elif choice == ord('7'):
            sorted_students = GPA.sorting(StudentManager.Student_list)
            for student in sorted_students:
                stdscr.addstr(f"ID: {student.student_id}, Name: {student.student_name}, GPA: {GPA.calculate_gpa(student)}\n")
        elif choice == ord('8'):
            break
        else:
            stdscr.addstr("Invalid choice.")

        stdscr.refresh()

    curses.endwin()

curses.wrapper(main)
