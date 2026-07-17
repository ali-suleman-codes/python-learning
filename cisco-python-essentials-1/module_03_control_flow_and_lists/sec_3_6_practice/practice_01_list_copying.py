# Statement

# A company stores employee IDs.
# [101, 102, 103, 104, 105]
# Create another list that is an independent copy of the original list using slicing.
# Change the first ID in the copied list to 999.
# Print both lists.

employee_ids = [101, 102, 103, 104, 105]

updated_ids = employee_ids[:]

updated_ids[0] = 999

print("Original :", employee_ids)
print("Copied   :", updated_ids)