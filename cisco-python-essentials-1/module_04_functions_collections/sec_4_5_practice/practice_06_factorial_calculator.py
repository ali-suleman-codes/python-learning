# Factorial Calculator
# Purpose:
# Calculate the factorial of a number using iteration.
# Concepts:
# - for loop
# - Accumulator
# - return

def factorial(num):
    if num < 0:
        return None
    if num < 2:
        return 1
    product = 1
    for i in range(2, num + 1):
        product *= i
    return product

print("5! :", factorial(5))