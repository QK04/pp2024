from domains import *
from input import *
from output import *
import curses

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

        choice = get_int_input(stdscr, "Enter your choice: ")

        if choice == 1:
            StudentManager.students_information(StudentManager,stdscr)
        elif choice == 2:
            CourseManager.courses_information(CourseManager,stdscr)
        elif choice == 3:
            StudentManager.list_students(StudentManager,stdscr)
        elif choice == 4:
            CourseManager.list_courses(CourseManager,stdscr)
        elif choice == 5:
            MarkManager.mark_information(MarkManager,stdscr)  
        elif choice == 6:
            MarkManager.list_mark(MarkManager, stdscr) 
        elif choice == 7:
            sorted_students = GPA.sorting(StudentManager.Student_list)
            for student in sorted_students:
                stdscr.addstr(f"ID: {student.student_id}, Name: {student.student_name}, GPA: {GPA.calculate_gpa(student)}\n")
        elif choice == 8:
            break
        else:
            stdscr.addstr("Invalid choice.")

curses.wrapper(main)