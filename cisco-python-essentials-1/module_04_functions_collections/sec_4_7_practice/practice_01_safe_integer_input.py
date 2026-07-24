# Safe Integer Input

# Purpose:
# Learn how to handle invalid integer input.

# Concepts:
# - try
# - except ValueError
# - int()

try :
    age = int(input("Enter age of student : "))
    print("Age :", age)
except ValueError:
    print("Invalid input : Age must be integer.")


