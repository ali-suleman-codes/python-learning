# Cinema Seating Chart

# Purpose:
# Display cinema seats row by row.

# Concepts:
# - Nested lists
# - Nested for loops

seating_chart = [
    ["A1", "A2", "A3", "A4"],
    ["B1", "B2", "B3", "B4"],
    ["C1", "C2", "C3", "C4"]
]

for row in seating_chart :
    for seat in row :
        print(seat, end = " ")
    print()