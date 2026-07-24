# Multiple Exception Handler

# Purpose:
# Handle different exceptions separately.

# Concepts:
# - Multiple except blocks
# - ValueError
# - ZeroDivisionError

try :
    numerator = int(input("Enter numerator : "))
    denominator = int(input("Enter denominator : "))
    print("Division : ", numerator / denominator)
except ZeroDivisionError:
    print("Invalid input : denominator must not be zero.")
except ValueError:
    print("Invalid input : Input must be integer.")
