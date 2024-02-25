from output import *

class Student:
    def __init__ (self, student_id, student_name, DoB):
        self.student_id = student_id            
        self.student_name = student_name
        self.DoB = DoB
        self.marks = []
    
    def add_mark(self, mark):
        self.marks.append(mark)

# Ask how many number of student and take student information      
class StudentManager:
    Student_list = []

    def students_information(cls, stdscr):
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
    def list_students(cls, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0,"List Students ")
        num = 1
        for student in cls.Student_list:
            stdscr.addstr(num, 0, f"Student {num}. ID: {student.student_id}, Name: {student.student_name}, Dob: {student.DoB}")
            num = num + 1
            stdscr.refresh()
            stdscr.getch()