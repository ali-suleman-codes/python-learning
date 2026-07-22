# Recursive Factorial Calculator
# Purpose:
# Learn how recursion works through factorial calculation.
# Concepts:
# - Recursion
# - Base case
# - return

def factorial(num):
    if num < 0:
        return None
    if num < 2:
        return 1
    return num * factorial(num - 1)

print("6! :", factorial(6))