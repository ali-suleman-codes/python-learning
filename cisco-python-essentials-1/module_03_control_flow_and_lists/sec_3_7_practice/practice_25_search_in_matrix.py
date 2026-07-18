# Search in Matrix

# Purpose:
# Search for a specific value inside a two-dimensional list.

# Concepts:
# - Nested lists
# - Nested loops
# - if statement

seating_log = [
    [101, 102, 103],
    [201, 202, 203],
    [301, 302, 303]
]

seat_number = int(input("Enter a seat number : "))
found = False
for row in seating_log:
    for seat_num in row :
        if seat_num == seat_number :
            found = True
            break
if found :
    print("Seat Found")
else :
    print("Seat Not Found")