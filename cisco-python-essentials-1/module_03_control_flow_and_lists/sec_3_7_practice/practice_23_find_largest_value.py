# Find Largest Value

# Purpose:
# Find the largest number in a two-dimensional list.

# Concepts:
# - Nested lists
# - Nested loops
# - Comparison

warehouse_package_weights = [
    [25, 10, 40],
    [15, 30, 18],
    [22, 35, 28]
]

largest_value = warehouse_package_weights[0][0]

for package in warehouse_package_weights :
    for weight in package:
        if weight > largest_value:
            largest_value = weight

print("Largest value :", largest_value)