# Recursive Fibonacci Calculator
# Purpose:
# Understand recursion by calculating Fibonacci numbers.
# Concepts:
# - Recursive functions
# - Base case
# - Function calls

def fibonacci(num):
    if num < 1:
        return None
    if num < 3:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

print("8th Fibonacci Number :", fibonacci(8))