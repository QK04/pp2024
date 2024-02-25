from domains import *
from output import *
import math

class Mark:
    def __init__ (self, student, course, mark):
        self.student = student
        self.course = course    
        self.mark = mark

# Select a course, input marks for student in this course
class MarkManager:
    Mark_list = []

    def mark_information(cls, stdscr):
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
    def list_mark (cls, stdscr):
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