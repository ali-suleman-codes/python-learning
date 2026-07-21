# Creating a New Student List
# Purpose:
# Understand that assigning a new list to a parameter does not change the original list.
# Concepts:
# - List assignment
# - Function parameters
# - Local variables
import sys
student_list = []
student_number = int(input("How many students : "))
if student_number < 1:
    print("Student number must be greater than zero")
    sys.exit()
for i in range(student_number):
    student_list.append(input(f"Enter name of student {i + 1} : "))

def update_list(student_list):
    student_list = ["Sara", "Fatima"]
    print("Inside function :", student_list)

update_list(student_list)
print("Outside function :", student_list)