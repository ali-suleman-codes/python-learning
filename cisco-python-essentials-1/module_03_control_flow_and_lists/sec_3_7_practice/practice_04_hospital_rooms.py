# Hospital Rooms

# Purpose:
# Represent hospital room numbers using a two-dimensional list and retrieve
# specific rooms using row and column indexes.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# A hospital has 2 floors and each floor contains 4 rooms.

hospital = [
    [11, 12, 13, 14],
    [21, 22, 23, 24]
]

print("Room 11 : ", hospital[0][0])
print("Room 23 : ", hospital[1][2])
print("Room 24 : ", hospital[1][3])
