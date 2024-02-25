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

#initialize curse
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

#Display a message
def display_message(message):
    stdscr.clear()
    stdscr.addstr(0, 0, message)
    stdscr.getch()

# Ask how many number of student and take student information      
class StudentManager:
    Student_list = []

    def students_information(cls):
        stdscr.clear()
        stdscr.addstr(0, 0, "Enter Number of Students: ")
        stdscr.refresh()
        s = int(stdscr.getstr().decode())

        if s <= 0:
            display_message("Error")
            return

        for i in range (1,s + 1):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Enter Student {i} ID: ")
            stdscr.refresh()
            student_id = stdscr.getstr().decode()

            for student in cls.Student_list:
                if student.student_id == student_id:
                    display_message("Already exist")
                    return      
                
            stdscr.addstr(1, 0, f"Enter Student {i} Name: ")
            stdscr.refresh()
            student_name = stdscr.getstr().decode()

            stdscr.addstr(2, 0, f"Enter Student {i} DoB: ")
            stdscr.refresh()
            DoB = stdscr.getstr().decode()

            cls.Student_list.append(Student(student_id, student_name, DoB))

# Display list students
    def list_students(cls):
        stdscr.clear()
        stdscr.addstr(0, 0,"List Students ")
        num = 1
        for student in cls.Student_list:
            stdscr.addstr(num, 0, f"Student {num}. ID: {student.student_id}, Name: {student.student_name}, Dob: {student.DoB}")
            num = num + 1
            stdscr.refresh()
            stdscr.getch()


# Ask how many number of course and take course information
class CourseManager:
    Course_list = []

    def courses_information(cls):
        stdscr.clear()
        stdscr.addstr(0, 0, "Enter Number of Courses: ")
        stdscr.refresh()
        c = int(stdscr.getstr().decode())

        if c <= 0:
            display_message("Error")
            return

        for i in range (1,c + 1):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Enter Course {i} ID: ")
            stdscr.refresh()
            course_id = stdscr.getstr().decode()
    
            for course in CourseManager.Course_list:
                if course.course_id == course_id:
                    display_message("Already exist")
                    return
                
            stdscr.addstr(1, 0, f"Enter Couse {i} Name: ")
            stdscr.refresh()
            course_name = stdscr.getstr().decode()

            stdscr.addstr(2, 0, f"Enter Credits for Course {i}: ")
            stdscr.refresh()
            credits = int(stdscr.getstr().decode())

            cls.Course_list.append(Course(course_id, course_name, credits))

    # Display list courses
    def list_courses(cls):
        stdscr.clear()
        stdscr.addstr(0, 0, "List Courses ")
        num = 1
        for course in cls.Course_list:
            stdscr.addstr(num, 0, f"Course {num}. ID: {course.course_id}, Name: {course.course_name}, Credits: {course.credits}")
            num = num + 1
        stdscr.refresh()
        stdscr.getch()

# Select a course, input marks for student in this course
class MarkManager:
    Mark_list = []

    def mark_information(cls):
        CourseManager.list_courses(CourseManager)
        stdscr.addstr(0,0, "Enter Course Name: ")
        stdscr.refresh()
        course_name = stdscr.getstr().decode()

        if course_name not in [course.course_name for course in CourseManager.Course_list]:
            display_message("Error")
            return    
        
        StudentManager.list_students(StudentManager)
        stdscr.addstr(0,0, "Enter Student Name: ")
        stdscr.refresh()
        student_name = stdscr.getstr().decode()

        if student_name not in [student.student_name for student in StudentManager.Student_list]:        
            display_message("Error")
            return
        
        course = next(course for course in CourseManager.Course_list if course.course_name == course_name)
        student = next(student for student in StudentManager.Student_list if student.student_name == student_name)
        
        stdscr.addstr(0,0, f"Input Mark for {student_name} in {course_name}: ")
        mark = float(stdscr.getstr().decode())
        round_down = math.floor(mark*10)/10

        cls.Mark_list.append(Mark(student, course, round_down))
        student.marks.append(Mark(student, course, round_down))

    # Display list marks
    def list_mark (cls):
        stdscr.clear()
        if not cls.Mark_list:
            stdscr.addstr(0, 0, "No marks available.")
            return        
        else:
            stdscr.addstr(0,0, "List of Marks:")
            for mark in cls.Mark_list:
                student_name = mark.student.student_name
                course_name = mark.course.course_name
                stdscr.addstr(0, 0, f"Course: {course_name}, Student: {student_name}, Mark: {mark.mark}")
        stdscr.refresh()
        stdscr.getch()

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
    while True:
        stdscr.clear()
        stdscr.addstr(1, 2, "1. Input student information: id, name, DoB")
        stdscr.addstr(2, 2, "2. Input course information: id, name")
        stdscr.addstr(3, 2, "3. List students")
        stdscr.addstr(4, 2, "4. List courses")
        stdscr.addstr(5, 2, "5. Select a course, input marks for student in this course")
        stdscr.addstr(6, 2, "6. Show student marks for a given course")
        stdscr.addstr(7, 2, "7. Sorting students by GPA")
        stdscr.addstr(8, 2, "8. Exit")
        stdscr.refresh()

        choice = stdscr.getch() - ord('0') 

        if choice == 1:
            StudentManager.students_information(StudentManager)
        elif choice == 2:
            CourseManager.courses_information(CourseManager)
        elif choice == 3:
            StudentManager.list_students(StudentManager)
        elif choice == 4:
            CourseManager.list_courses(CourseManager)
        elif choice == 5:
            MarkManager.mark_information(MarkManager)  
        elif choice == 6:
            MarkManager.list_mark(MarkManager) 
        elif choice == 7:
            sorted_students = GPA.sorting(StudentManager.Student_list)
            for student in sorted_students:
                stdscr.addstr(f"ID: {student.student_id}, Name: {student.student_name}, GPA: {GPA.calculate_gpa(student)}\n")
        elif choice == 8:
            break
        else:
            stdscr.addstr("Invalid choice.")

curses.wrapper(main)
