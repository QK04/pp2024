from output import *

class Student:
    def __init__ (self, student_id, student_name, DoB):
        self.student_id = student_id            
        self.student_name = student_name
        self.DoB = DoB
        self.marks = []
    
    def add_mark(self, mark):
        self.marks.append(mark)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.student_name}, DoB: {self.DoB}"