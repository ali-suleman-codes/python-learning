# Airline Seating

# Purpose:
# Represent airplane seating using a nested list.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# An airline has 3 rows and each rows 4 seats

airline_seating = [
    ["A1", "A2", "A3", "A4"],
    ["B1", "B2", "B3", "B4"],
    ["C1", "C2", "C3", "C4"]
]

print("Row 1     :", airline_seating[0])
print("Seat B3   :", airline_seating[1][2])
print("Seat C1   :", airline_seating[2][0])
print("Last seat :", airline_seating[2][3])
