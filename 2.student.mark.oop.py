class Student:
    def __init__ (self, student_id, student_name, DoB):
        self.student_id = student_id            
        self.student_name = student_name
        self.DoB = DoB

class Course:
    def __init__ (self, course_id, course_name):
        self.course_name = course_name
        self.course_id = course_id    

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
            course_name = str(input("Enter Couse %d Name: " %i))
            cls.Course_list.append(Course(course_id, course_name))

    # Display list courses
    def list_courses(cls):
        print("\nList Courses ")
        num = 1
        for course in cls.Course_list:
            print(f"Course {num}. ID: {course.course_id}, Name: {course.course_name}")
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
        
        mark = float(input(f"Input Mark for {student_name} in {course_name}: "))
        cls.Mark_list.append(Mark(Student(student_name, "", ""), Course(course_name, ""), mark))

    # Display list marks
    def list_mark (cls):
        CourseManager.list_courses(CourseManager)
        course_name = str(input("Enter Course Name: "))
        if course_name not in [course.course_name for course in CourseManager.Course_list]:
            print("Error")
            return
        
        print(f"\nList Marks for Course: {course_name}")
        for mark_dict in cls.Mark_list:        
            if mark_dict.course.course_name == course_name:
                student_name = mark_dict.student.student_name
                mark = mark_dict.mark
                print(f"Student Name: {student_name} \nMark: {mark}")

# Main function:  Student Mark Management
while True:
    print("\n1. Input student information: id, name, DoB")
    print("2. Input course information: id, name")
    print("3. List students")
    print("4. List courses")
    print("5. Select a course, input marks for student in this course")
    print("6. Show student marks for a given course")
    print("7. Exit")

    choice = int(input("Choose: "))

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
        exit()
    else:
        print("Invalid choice.")






