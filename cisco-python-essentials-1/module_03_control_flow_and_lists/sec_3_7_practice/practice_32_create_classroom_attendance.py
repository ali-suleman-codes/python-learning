# Create Classroom Attendance

# Purpose:
# Create a classroom attendance grid.

# Concepts:
# - Nested list comprehension
# - Matrix creations

# Create a 3 × 5 attendance sheet where every value is initially "Absent".

class_attendance = [["Absent" for _ in range(5)] for _ in range(3)]

for row in class_attendance:
    for attendance in row :
        print(attendance, end = " ")
    print()