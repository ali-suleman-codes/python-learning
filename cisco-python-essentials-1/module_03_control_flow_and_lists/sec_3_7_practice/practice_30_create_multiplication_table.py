# Create Multiplication Table

# Purpose:
# Create a multiplication table using nested list comprehension.

# Concepts:
# - Nested list comprehension
# - range()

multiplication_table = [[i*j for i in range(1, 4)] for j in range(1, 4)]

for row in multiplication_table :
    for number in row :
        print(number , end = " ")
    print()
