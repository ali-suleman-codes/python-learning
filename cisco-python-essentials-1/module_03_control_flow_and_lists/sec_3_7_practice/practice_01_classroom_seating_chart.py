# Classroom Seating Chart

# Purpose:
# Store a classroom seating arrangement in a two-dimensional list and access
# students using row and column indexes.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# A school has 3 rows of benches and each row has 4 students
seating_arrangement = [
    ["Ali", "Ahmad", "Bilal", "Usman"],
    ["Hamza", "Saad", "Zain", "Umar"],
    ["Ayan", "Hassan", "Daniyal", "Huzaifa"]
]

print("Complete seating : ")
print(seating_arrangement)

print("First Row First Column  :", seating_arrangement[0][0])
print("Second Row Third Column :", seating_arrangement[1][2])
print("Last Row Last Column    :", seating_arrangement[2][3])