# Reducing Repeated Code

# Purpose:
# Replace duplicated print statements with one reusable function.

# Concepts:
# - Function reuse
# - Code repetition
# - Function invocation

def prompt():
    print("Please enter a value : ")


prompt()
val1 = int(input())

prompt()
val2 = int(input())

prompt()

val3 = int(input())

print("Value 1 :", val1)
print("Value 2 :", val2)
print("Value 3 :", val3)