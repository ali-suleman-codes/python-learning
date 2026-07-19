# Employee ID Card Generator

# Purpose:
# Compare positional and keyword argument passing.

# Concepts:
# - Positional arguments
# - Keyword arguments
# - Function calls

def employee_info(name, department, employee_id):
    print("Name : " + name + " | Department : " + department + " | Id :", employee_id)

employee_info("Ali", "Computer Science", 1234)
employee_info(employee_id = 2456, name = "King", department = "Physics")
employee_info("Azeem", "Pharm - D", employee_id = 9733)