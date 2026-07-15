# Problem Statement

# Ask the user to enter two integers.

# Display:

# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Modulus
# Exponentiation

num1 = int(input("Enter 1st integer : "))
num2 = int(input("Enter 2nd integer : "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = round(num1 / num2, 2)
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

print("\nAddition       :", addition)
print("Subtraction    :", subtraction)
print("Multiplication :", multiplication)
print("Division       :", division)
print("Floor division :", floor_division)
print("Modulus        :", modulus)
print("Exponentiation :", exponentiation)