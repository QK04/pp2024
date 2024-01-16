# Create a list to add students, courses, mark
Student = []
Course = []
Mark = []

# Ask how many number of student and take student information
def students_information():
    s = int(input("Enter Number of Students: "))
    if s <= 0:
        print("Error")
        return

    for i in range (1,s + 1):
        student_dict = {}
        student_id = str(input("\nEnter Student %d ID: " %i))
        student_name = str(input("Enter Student %d Name: " %i))
        student_DoB = str(input("Enter Student %d DoB: " %i))
        
        student_dict.update({"ID":student_id, "Name":student_name, "DoB":student_DoB})
        Student.append(student_dict)

# Display list students
def list_students():
    print("\nList Students ")
    num = 1
    for student_dict in Student:
        student_id = student_dict.get("ID")
        student_name = student_dict.get("Name")
        student_DoB = student_dict.get("DoB")

        print(f"Student {num}. ID: {student_id}, Name: {student_name}, Dob: {student_DoB}")
        num = num + 1

# Ask how many number of course and take course information
def course_information():
    c = int(input("\nEnter Number of Courses: "))

    if c <= 0:
        print("Error")
        return

    for i in range (1,c + 1):
        course_dict = {}
        course_id = str(input("\nEnter Course %d ID: " %i))
        course_name = str(input("Enter Couse %d Name: " %i))
        
        course_dict.update({"ID":course_id, "Name":course_name})
        Course.append(course_dict)

# Display list courses
def list_courses():
    print("\nList Courses ")
    num = 1
    for course_dict in Course:
        course_id = course_dict.get("ID")
        course_name = course_dict.get("Name")

        print(f"Course {num}. ID: {course_id}, Name: {course_name}")
        num = num + 1

# Select a course, input marks for student in this course
def mark_information():
    list_courses()
    course_name = str(input("Enter Course Name: "))
    if course_name not in [course['Name'] for course in Course]:
        print("Error")
        return    
    
    list_students()
    student_name = str(input("Enter Student Name: "))
    if student_name not in [student['Name'] for student in Student]:        
        print("Error")
        return
    
    mark = float(input(f"Input Mark for {student_name} in {course_name}: "))
    Mark.append({"Student Name":student_name, "Course Name":course_name, "Mark":mark})

# Display list marks
def list_mark (Mark):
    list_courses()
    course_name = str(input("Enter Course Name: "))
    if course_name not in [course['Name'] for course in Course]:
        print("Error")
        return
    
    print(f"\nList Marks for Course: {course_name}")
    for mark_dict in Mark:        
        if mark_dict.get("Course Name") == course_name:
            student_name = mark_dict.get("Student Name")
            mark = mark_dict.get("Mark")
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
        students_information()
    elif choice == 2:
        course_information()
    elif choice == 3:
        list_students()
    elif choice == 4:
        list_courses()
    elif choice == 5:
        mark_information()  
    elif choice == 6:
        list_mark(Mark)  
    elif choice == 7:
        exit()
    else:
        print("Invalid choice.")






