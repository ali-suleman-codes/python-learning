# Triangle Validator
# Purpose:
# Determine whether three sides can form a valid triangle.
# Concepts:
# - Boolean return values
# - Logical operators
# - Multiple parameters

def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

if is_triangle(3, 2, 4):
    print("Valid Triangle")
else :
    print("Invalid Triangle")