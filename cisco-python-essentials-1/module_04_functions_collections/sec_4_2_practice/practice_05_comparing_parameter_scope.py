# Comparing Parameter Scope

# Purpose:
# Understand that parameters exist only inside the function and can shadow variables with the same name.

# Concepts:
# - Parameter scope
# - Shadowing
# - Local parameter

department = "Sales"

def department_info(department) :
    print("Inside function  : " + department)

print("Outside function : " + department)
department_info("Management")
print("Outside function : " + department)