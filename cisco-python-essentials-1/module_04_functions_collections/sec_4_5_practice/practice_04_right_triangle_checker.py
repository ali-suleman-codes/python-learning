# Right Triangle Checker
# Purpose:
# Determine whether a valid triangle is a right-angled triangle.
# Concepts:
# - Calling another function
# - Pythagorean theorem
# - Boolean return values

def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_right_angle(a, b, c):
    if not is_triangle(a, b, c):
        return None
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > c and b > a:
        return b ** 2 == a ** 2 + c ** 2
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    
result = is_right_angle(3, 4, 5)
if result is None:
    print("Invalid Triangle")
elif result:
    print("Right Triangle")
else :
    print("Not a Right Triangle")