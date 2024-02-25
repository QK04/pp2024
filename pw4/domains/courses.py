from output import *

class Course:
    def __init__ (self, course_id, course_name, credits):
        self.course_name = course_name
        self.course_id = course_id    
        self.credits = credits

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