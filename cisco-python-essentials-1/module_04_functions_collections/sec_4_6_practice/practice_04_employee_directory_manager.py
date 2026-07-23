# Employee Directory Manager
# Purpose:

# Practice modifying dictionary contents.

# Concepts:
# Updating values
# Adding keys
# update()
# del
# popitem()

employee = {
    "Ali" : "Marketing",
    "Azeem" : "Front-end",
    "King" : "Back-end"
}

employee["Ali"] = "Back-end"

employee["Kamran"] = "Marketing"

employee.update({"Queen" : "Front-end"})

del employee["Azeem"]

employee.popitem()

print("Updated final dictionary :", employee)