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
    char_grade = ""
    if 'round' in ksuffix and ksuffix['round'] == True:
        grade = rounding(grade)
    if grade >= 90:
        char_grade = "A"
    elif 80 <=  grade < 90:
        char_grade = "B"
    elif 70 <=  grade < 80:
        char_grade = "C"
    elif 60 <=  grade < 70:
        char_grade = "D"
    else:
        return "F"
    if 'suffix' in ksuffix and ksuffix['suffix'] == True:
        if re.search("\..", str(grade)):
            grade = int(re.sub("\..", "", str(grade)))
        if re.search("(7|8|9|00)$", str(grade)):
            char_grade += "+"
        elif re.search("(0|1|2)$", str(grade)):
            char_grade += "-"
    return char_grade

def calculate_gpa(grade_list):
    total_value = 0
    for value in grade_list:
        if re.search("A", value):
            total_value += 4
        elif re.search("B", value):
            total_value += 3
        elif re.search("C", value):
            total_value += 2
        elif re.search("D", value):
            total_value += 1
        if re.search("\+", value):
            total_value += 0.33
        elif re.search("\-", value):
            total_value -= 1
            total_value += 0.67
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