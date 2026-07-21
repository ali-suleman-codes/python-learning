# Updating a Global Variable
# Purpose:
# Learn how to modify a global variable using the global keyword.
# Concepts:
# - global keyword
# - Global scope
# - Variable modification

manager = "Ali"
print("Current Manager :", manager)

def update_manager():
    global manager
    manager = "Ahmed"

update_manager()
print("Updated Manager :", manager)