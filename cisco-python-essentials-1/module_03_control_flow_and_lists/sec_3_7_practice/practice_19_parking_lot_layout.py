# Parking Lot Layout

# Purpose:
# Display parking slots using nested loops.

# Concepts:
# - Nested lists
# - Nested for loops

parking_layout = [
    ["P01", "P02", "P03", "P04"],
    ["P05", "P06", "P07", "P08"],
    ["P09", "P10", "P11", "P12"]
]

for row in parking_layout :
    for parking in row :
        print(parking, end = " ")
    print()