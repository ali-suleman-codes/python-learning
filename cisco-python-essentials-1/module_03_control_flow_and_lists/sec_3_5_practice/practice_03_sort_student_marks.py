# Statement
# Ask the user to enter five employee salaries.
# Store them in a list.
# Sort them using Bubble Sort.
# Print both the original and sorted lists.

employee_salaries = []
for i in range(5):
    employee_salaries.append(int(input(f"Enter salary of employee {i + 1} : ")))

print("Original salaries :", employee_salaries)

for i in range(len(employee_salaries) - 1) :
    swapped = False    

    for j in range(len(employee_salaries) - 1 - i) :
        if employee_salaries[j] > employee_salaries[j + 1] :
            swapped = True
            employee_salaries[j], employee_salaries[j + 1] = employee_salaries[j + 1], employee_salaries[j]
    
    if not swapped :
        break

print("Sorted salaries :", employee_salaries)