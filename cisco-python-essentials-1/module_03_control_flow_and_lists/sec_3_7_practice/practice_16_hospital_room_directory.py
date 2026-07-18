# Hospital Room Directory

# Purpose:
# Display room numbers floor by floor.

# Concepts:
# - Nested lists
# - Nested for loops

hospital_room_directory = [
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34],
]

for floor in hospital_room_directory :
    for room in floor :
        print(room, end = " ")
    print()