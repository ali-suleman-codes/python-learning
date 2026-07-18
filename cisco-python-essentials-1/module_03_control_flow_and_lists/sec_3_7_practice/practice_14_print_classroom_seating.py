# Classroom Seating

# Purpose:
# Print every student in a classroom using nested for loops.

# Concepts:
# - Nested lists
# - Nested for loops
# - Row traversal
# - Column traversal

# A class room has 3 rows and each row has 4 students
class_room_seating = [
    ["Ali", "Ahmad", "Bilal", "Usman"],
    ["Hamza", "Saad", "Zain", "Umar"],
    ["Ayan", "Hassan", "Daniyal", "Huzaifa"]
]

for row in class_room_seating :
    for student in row :
        print(student , end = "  ")
    print()