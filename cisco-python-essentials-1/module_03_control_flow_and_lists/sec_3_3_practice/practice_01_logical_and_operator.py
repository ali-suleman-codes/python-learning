# Goal
# Ask the user to enter:
# Age
# Has ID Card (yes/no)
# Display:
# Eligible
# only if:
# age is at least 18 and
# user has an ID card.

age = int(input("Enter age : "))
input_id = input("Do you have id card(yes/no) ? ").lower()

has_id = (input_id == "yes")
if (age >= 18) and has_id :
    print("Eligible")
else :
    print("Not eligible")