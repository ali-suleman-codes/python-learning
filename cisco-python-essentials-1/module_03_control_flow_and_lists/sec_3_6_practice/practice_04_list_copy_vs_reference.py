# Statement
# A school keeps a list of classroom numbers.
# [1, 2, 3, 4]
# Create
# one variable using normal assignment
# another using slicing
# Modify the first element of both new lists.
# Print all three lists and observe the difference.

class_numbers = [1, 2, 3, 4]

class_numbers_list = class_numbers

list_class_numbers = class_numbers[:]

class_numbers_list[0] = 9 # Due to normal assignment value at index 1 will change for both class_numbers and class_numbers_list
list_class_numbers[0] = 10

print("Original :", class_numbers) 
print("Assigned :", class_numbers_list)
print("Copied   :", list_class_numbers)