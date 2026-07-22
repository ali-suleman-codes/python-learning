# Body Mass Index (BMI) Calculator
# Purpose:
# Calculate the Body Mass Index (BMI) using weight and height.
# Concepts:
# - Multiple parameters
# - Returning values
# - Input validation
# - if statement

def calculate_bmi(weight, height):
    if height <= 1.0 or height >= 2.5 or \
    weight <= 20 or weight >= 200 :
        return None
    return weight / height ** 2

result = calculate_bmi(63, 1.5)
print("BMI :", result)