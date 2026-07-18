# Count Specific Value

# Purpose:
# Count how many times a value appears in a two-dimensional list.

# Concepts:
# - Nested lists
# - Nested loops
# - Counter

factory_quality_inspection = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]
total_passed = 0
total_failed = 0

for row in factory_quality_inspection :
    for result in row :
        if result == 1 :
            total_passed += 1
        else :
            total_failed += 1


print("Total Passed :", total_passed)
print("Total Failed :", total_failed)
