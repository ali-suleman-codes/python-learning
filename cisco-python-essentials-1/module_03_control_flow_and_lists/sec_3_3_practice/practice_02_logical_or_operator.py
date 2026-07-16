# Goal
# Ask the user:
# Are you a student? (yes/no)
# Are you a senior citizen? (yes/no)
# Display:
# Discount Available
# if either answer is yes.

input_student = input("Are you a student (yes/no) ? ").lower()
input_senior_citizen = input("Are you a senior citizen (yes/no) ? ").lower()

is_student = (input_student == "yes")
is_senior_citizen = (input_senior_citizen == "yes")

if is_student  or is_senior_citizen:
    print("Discount available")
else :
    print("Discount available")