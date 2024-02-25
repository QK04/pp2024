import numpy as np
import math

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