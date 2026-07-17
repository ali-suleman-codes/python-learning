# Apartment Building

# Purpose:
# Store apartment numbers in a two-dimensional list and retrieve apartments
# using row and column indexes.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# A building has 3 floors and each floor has 3 apartments.

building = [
    [101, 102, 103],
    [201, 202, 203],
    [301, 302, 303]
]

print("First Floor First apartment   :", building[0][0])
print("Second Floor Middle apartment :", building[1][1])
print("Last Floor Last apartment     :", building[2][2])
