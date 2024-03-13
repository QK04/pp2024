import tkinter as tk
from input import *

class App:
    def __init__(self, master):
        self.master = master
        master.title("Student Management System")
        master.geometry("800x600")

        self.label = tk.Label(master, text="Welcome to Student Management System")
        self.label.pack()

        self.button_students = tk.Button(master, text="Input Student Information", command=self.input_students)
        self.button_students.pack()

        self.button_courses = tk.Button(master, text="Input Course Information", command=self.input_courses)
        self.button_courses.pack()

        self.button_list_students = tk.Button(master, text="List Students", command=self.list_students)
        self.button_list_students.pack()

        self.button_list_courses = tk.Button(master, text="List Courses", command=self.list_courses)
        self.button_list_courses.pack()

        self.button_marks = tk.Button(master, text="Input Marks", command=self.input_marks)
        self.button_marks.pack()

        self.button_list_marks = tk.Button(master, text="List Marks", command=self.list_marks)
        self.button_list_marks.pack()

        self.button_sort_students = tk.Button(master, text="Sort Students by GPA", command=self.sort_students)
        self.button_sort_students.pack()

        self.button_exit = tk.Button(master, text="Exit", command=master.quit)
        self.button_exit.pack()

    def input_students(self):
        StudentManager.students_information()
        pass

    def input_courses(self):
        CourseManager.courses_information()
        pass

    def list_students(self):
        StudentManager.list_students()
        pass

    def list_courses(self):
        CourseManager.list_courses()
        pass

    def input_marks(self):
        MarkManager.mark_information()
        pass

    def list_marks(self):
        MarkManager.list_mark()
        pass

    def sort_students(self):
        sorted_students = GPA.sorting(StudentManager.Student_list)
        for student in sorted_students:
            student_GPA = GPA.calculate_gpa(student)
            print(f"ID: {student.student_id}, Name: {student.student_name}, GPA: {student_GPA}")
        pass

def main():
    decompress_file()
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    compress_file()

if __name__ == "__main__":
    main()
