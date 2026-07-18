# Create Identity Matrix

# Purpose:
# Generate an identity matrix.

# Concepts:
# - Nested list comprehension
# - Conditional expression

identity_matrix = [[1 if i == j else 0 for i in range(4)] for j in range(4)]

for row in identity_matrix :
    for value in row :
        print(value , end = " ")
    print()