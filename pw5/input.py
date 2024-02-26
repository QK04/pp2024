from output import *
from domains import *
import math
import numpy as np
import os
import zipfile

def get_int_input(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(0, 0, prompt)
    stdscr.refresh()


def get_string_input(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(0, 0, prompt)
    stdscr.refresh()

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

        write_to_file("Students.txt", '\n'.join([str(student) for student in cls.Student_list]))

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

# Ask how many number of course and take course information
class CourseManager:
    Course_list = []

    def courses_information(cls, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Enter Number of Courses: ")
        stdscr.refresh()
        c = int(stdscr.getstr().decode())

        if c <= 0:
            display_message(stdscr, "Error")
            return

        for i in range (1,c + 1):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Enter Course {i} ID: ")
            stdscr.refresh()
            course_id = stdscr.getstr().decode()
    
            for course in CourseManager.Course_list:
                if course.course_id == course_id:
                    display_message(stdscr, "Already exist")
                    return
                
            stdscr.addstr(1, 0, f"Enter Couse {i} Name: ")
            stdscr.refresh()
            course_name = stdscr.getstr().decode()

            stdscr.addstr(2, 0, f"Enter Credits for Course {i}: ")
            stdscr.refresh()
            credits = int(stdscr.getstr().decode())

            cls.Course_list.append(Course(course_id, course_name, credits))
        
        write_to_file("Courses.txt", '\n'.join([str(course) for course in cls.Course_list]))

    # Display list courses
    def list_courses(cls, stdscr):
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

    def mark_information(cls, stdscr):
        stdscr.addstr(0,0, "Enter Course Name: ")
        stdscr.refresh()
        course_name = stdscr.getstr().decode()

        if course_name not in [course.course_name for course in CourseManager.Course_list]:
            display_message("Error")
            return    
        
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

        write_to_file("Marks.txt", '\n'.join([str(mark) for mark in cls.Mark_list]))

    # Display list marks
    def list_mark (cls, stdscr):
        stdscr.clear()
        if not cls.Mark_list:
            stdscr.addstr(0, 0, "No marks available.")
            return        
        else:
            stdscr.addstr(0,0, "List of Marks:")
            num = 1
            for mark in cls.Mark_list:
                student_name = mark.student.student_name
                course_name = mark.course.course_name
                stdscr.addstr(num, 0, f"Course: {course_name}, Student: {student_name}, Mark: {mark.mark}")
                num = num + 1
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

def write_to_file(filename, data):
    with open(filename,'a') as file:
        file.write(data + '\n')

def compress_file():    
    try:
        with zipfile.ZipFile('student.dat','w') as zip:
            zip.write('students.txt')
            zip.write('courses.txt')
            zip.write('marks.txt')
    except IOError as e:
        print(f"Error compressing files: {e}")
    
def decompress_file():
    if os.path.exists('students.dat'):
        try:
            with zipfile.ZipFile('students.dat','r') as zip:
                zip.extractall('.')
        except IOError as e:
            print(f"Error decompressing files: {e}")  

def get_student_info(prompt):
    student_id = get_string_input(prompt, "Enter student ID: ")
    student_name = get_string_input(prompt, "Enter student name: ")
    DoB = get_string_input(prompt, "Enter DoB: ")
    student_info = f"{student_id}, {student_name}, {DoB}"
    write_to_file("students.txt", student_info)
    return student_info

def get_course_info(prompt):
    course_id = get_string_input(prompt, "Enter course ID: ")
    course_name = get_string_input(prompt, "Enter course name: ")
    credits = get_string_input(prompt, "Enter credits: ")
    course_info = f"{course_id}, {course_name}, {credits}"
    write_to_file("courses.txt", course_info)
    return course_info

def get_mark_info(prompt):
    course_name = get_string_input(prompt, "Enter course name: ")
    student_name = get_string_input(prompt, "Enter student name: ")
    mark = get_int_input(prompt, "Enter mark: ")
    mark_info = f"{course_name}, {student_name}, {mark}"
    write_to_file("marks.txt", mark_info)
    return mark_info

