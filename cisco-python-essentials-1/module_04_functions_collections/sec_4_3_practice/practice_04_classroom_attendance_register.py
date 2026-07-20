# Classroom Attendance Register
# Purpose:
# Learn how to pass a list to a function.
# Concepts:
# - Lists as arguments
# - for loop
# - Functions

def display_student_names(present_students):
    print("List of present students : ")
    for i in range(len(present_students)):
        print(f"Student {i + 1} : ", present_students[i])

student_number = int(input("Enter how many students : "))
present_students = []

for i in range(student_number):
    present_students.append(input(f"Enter name of student {i + 1} : "))

display_student_names(present_students)



