# Triangle Area Calculator
# Purpose:
# Calculate the area of a valid triangle using Heron's formula.
# Concepts:
# - Helper functions
# - Function reuse
# - Returning values

def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_triangle(a, b, c):
    if not is_triangle(a, b, c):
        return None
    return heron(a, b, c)

print("Triangle Area :", area_of_triangle(4, 5, 4))

