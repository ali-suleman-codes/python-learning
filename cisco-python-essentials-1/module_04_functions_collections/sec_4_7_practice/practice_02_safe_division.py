# Safe Division Calculator

# Purpose:
# Prevent program crashes caused by division by zero.

# Concepts:
# - try
# - except ZeroDivisionError
# - Arithmetic operations

try :
    numerator = int(input("Enter numerator : "))
    denominator = int(input("Enter denumerator : "))
    print("Division : ", numerator / denominator)
except ZeroDivisionError:
    print("Invalid input : Denumerator must not be zero.")