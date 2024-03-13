class Mark:
    def __init__ (self, student, course, mark):
        self.student = student
        self.course = course    
        self.mark = mark

    def __str__(self):
        return f"Student: {self.student.student_name}, Course: {self.course.course_name}, Mark: {self.mark}"
