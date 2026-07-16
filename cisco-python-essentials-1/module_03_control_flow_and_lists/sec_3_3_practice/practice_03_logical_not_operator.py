# Goal
# Ask the user:
# Do you have an account? (yes/no)
# If the answer is no, display:
# Please create an account.
# Otherwise display:
# Login successful.
# Use the not operator.

input_account = input("Do you have an account (yes/no) ? ").lower()
has_account = (input_account == "yes")
if  not has_account :
    print("Please create an account.")
else :
    print("Login successful")