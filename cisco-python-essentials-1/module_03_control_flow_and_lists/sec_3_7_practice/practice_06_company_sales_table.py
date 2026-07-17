# Company Sales Table

# Purpose:
# Store monthly sales of three company branches and retrieve
# complete rows and specific sales values.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# A company has 3 branches and each branch records sales for 4 months.

branch_sales = [
    [120, 150, 180, 170],
    [140, 160, 190, 200],
    [130, 145, 175, 185]
]

print("Branch 1 :", branch_sales[0])
print("Branch 3 :", branch_sales[2])

print("Branch 2 month 2 :", branch_sales[1][1])
print("Branch 1 month 4 :", branch_sales[0][3])