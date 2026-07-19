# Building a Small Program with Functions

# Purpose:
# Organize a program into small reusable functions.

# Concepts:
# - Multiple functions
# - Decomposition
# - Function calls
# - Input
# - print()


def display_title():
    print("King Grocery Store")

def ask_customer_name() :
    print("Enter customer name : ", end = " ")

def display_goodbye():
    print("GoodBye", end = " ")

display_title()
ask_customer_name()
customer_name = input()
display_goodbye()
print(customer_name)


