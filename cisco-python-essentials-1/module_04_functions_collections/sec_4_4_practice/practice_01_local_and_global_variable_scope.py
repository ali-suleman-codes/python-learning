# Local and Global Variable Scope
# Purpose:
# Understand the difference between local and global variables.
# Concepts:
# - Local variables
# - Global variables
# - Variable shadowing

office = "Lahore"

def office_location():
    print("Office :", office)

def office_location_update():
    office = "Karachi"
    print("Office :", office)

office_location()
office_location_update()
print("Office :", office)