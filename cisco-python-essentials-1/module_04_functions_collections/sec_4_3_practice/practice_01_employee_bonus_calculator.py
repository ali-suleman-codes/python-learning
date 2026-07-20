# Employee Bonus Calculator
# Purpose:
# Learn how to return a calculated value from a function.
# Concepts:
# - return with expression
# - Function result
# - Assigning returned values

def calculate_bonus(salary):
    bonus_rate = 0.15
    return bonus_rate * salary

salary = float(input("Enter employee salary : "))
bonus = calculate_bonus(salary)
print(f"Employee Bonus : {bonus : .2f}")



