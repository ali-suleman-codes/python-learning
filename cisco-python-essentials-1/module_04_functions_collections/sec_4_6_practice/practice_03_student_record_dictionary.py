# Student Record Dictionary
# Purpose:

# Learn how to create, access, and safely search a dictionary.

# Concepts:
# Dictionary creation
# Key-value pairs
# Dictionary indexing
# in
# not in

student_record = {
    1234 : "Ali",
    2345 : "King",
    3456 : "Azeem"
}

roll_no = int(input("Enter a roll no : "))
if roll_no in student_record:
    print(f"Student found : {student_record[roll_no]}")
else :
    print("Student not found")
