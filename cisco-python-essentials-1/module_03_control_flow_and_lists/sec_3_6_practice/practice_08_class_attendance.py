# Statement
# A classroom attendance list contains
# ["Ali", "Ahmed", "Usman", "Bilal"]
# Ask the user to enter a student's name.
# If the student is in the list, print
# Present
# Otherwise print
# Absent

attendance_list = ["Ali", "Ahmed", "Usman", "Bilal"]
student = input("Enter student name : ")

if student in attendance_list :
    print("Present")
else : 
    print("Absent")