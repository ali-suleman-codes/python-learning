# Student Attendance List Manager
# Purpose:
# Understand how modifying a list inside a function affects the original list.
# Concepts:
# - Lists
# - Mutable objects
# - Function arguments
import sys
student_list = []
student_number = int(input("How many students : "))
if student_number < 1:
    print("Student number must be greater than zero")
    sys.exit()
for i in range(student_number):
    student_list.append(input(f"Enter name of student {i + 1} : "))

def update_list(student_list):
    del student_list[0]
    print("Inside function :", student_list)

update_list(student_list)
print("Outside function :", student_list)