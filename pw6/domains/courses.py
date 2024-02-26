class Course:
    def __init__ (self, course_id, course_name, credits):
        self.course_name = course_name
        self.course_id = course_id    
        self.credits = credits
        
    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.course_name}, Credits: {self.credits}"
