# Weekly Sales Report

# Purpose:
# Print sales data using nested loops.

# Concepts:
# - Nested lists
# - Nested for loops

sales_report = [
    [120, 150, 180, 170],
    [140, 160, 190, 200],
    [130, 145, 175, 185],
]

for branch in sales_report:
    for sale in branch :
        print(sale, end = " ")
    print()