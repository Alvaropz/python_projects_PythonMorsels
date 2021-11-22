#Python Morsels

import math
import re

def rounding(grade):
    decimal_part = grade - int(grade)
    if decimal_part >= 0.5:
        grade = math.ceil(grade)
    else:
        grade = math.floor(grade)
    return grade

def percent_to_grade(grade, **ksuffix):
    if 'round' in ksuffix and ksuffix['round'] == True:
        grade = rounding(grade)
    if grade >= 90:
        if 'suffix' in ksuffix and ksuffix['suffix'] == True:
            if grade >= 97:
                return "A+"
            elif grade < 93:
                return "A-"
        return "A"
    elif 80 <=  grade < 90:
        if 'suffix' in ksuffix and ksuffix['suffix'] == True:
            if grade >= 87:
                return "B+"
            elif grade < 83:
                return "B-"
        return "B"
    elif 70 <=  grade < 80:
        if 'suffix' in ksuffix and ksuffix['suffix'] == True:
            if grade >= 77:
                return "C+"
            elif grade < 73:
                return "C-"
        return "C"
    elif 60 <=  grade < 70:
        if 'suffix' in ksuffix and ksuffix['suffix'] == True:
            if grade >= 67:
                return "D+"
            elif grade < 63:
                return "D-"
        return "D"
    else:
        return "F"

def calculate_gpa(grade_list):
    total_value = 0
    for value in grade_list:
        if value == "A+":
            total_value += 4.33
        elif value == "A":
            total_value += 4.00
        elif value == "A-":
            total_value += 3.67
        elif value == "B+":
            total_value += 3.33
        elif value == "B":
            total_value += 3.00
        elif value == "B-":
            total_value += 2.67
        elif value == "C+":
            total_value += 2.33
        elif value == "C":
            total_value += 2.00
        elif value == "C-":
            total_value += 1.67
        elif value == "D+":
            total_value += 1.33
        elif value == "D":
            total_value += 1.00
        elif value == "D-":
            total_value += 0.67
        elif value == "F":
            total_value += 0.00
    return total_value/len(grade_list)

print(percent_to_grade(97)) #A
print(percent_to_grade(80)) #B
print(percent_to_grade(60.00001)) #D
print(percent_to_grade(59.9)) #F
print(percent_to_grade(92, suffix=True)) #A-
print(percent_to_grade(98, suffix=True)) #A+
print(percent_to_grade(95, suffix=True)) #A
print(percent_to_grade(100, suffix=True)) #A+
print(percent_to_grade(0, suffix=True)) #F
print(percent_to_grade(89.5, suffix=True, round=True)) #A-
print(percent_to_grade(92.5, suffix=True, round=True)) #A
print(percent_to_grade(72.6, suffix=True)) #C-
print(calculate_gpa(['A', 'B', 'C', 'D', 'F'])) #2.0
print(calculate_gpa(['A-', 'B+', 'C', 'D+', 'F'])) #2.066