# Student Marks Report

# Purpose:
# Display marks of every student.

# Concepts:
# - Nested lists
# - Nested for loops

marks_report = [
    [78, 82, 91],
    [67, 74, 80],
    [88, 90, 95]
]

for student_number, student in enumerate(marks_report, start = 1) :
    print(f"Student {student_number} :")
    for marks in student :
        print(marks)
    print()