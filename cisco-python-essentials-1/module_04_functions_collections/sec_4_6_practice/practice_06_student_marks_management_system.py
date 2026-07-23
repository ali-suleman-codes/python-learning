# Student Marks Management System
# Purpose:

# Combine tuples and dictionaries to store and process multiple values.

# Concepts:
# Tuples
# Dictionaries
# Tuple concatenation
# Dictionary membership
# sorted()
# Nested for loop
# Average calculation

student_record = {}
while True:
    name = input("Enter a student name : ")
    if name == "":
        break
    score = int(input("Enter score(0-10) : "))
    if score not in range(0, 11):
        break
    if name in student_record:
        student_record[name] += (score,)
    if name not in student_record:
        student_record[name] = (score,)


for key, value in sorted(student_record.items()):
    count = 0
    add = 0
    for score in value:
        add += score
        count += 1
    average = add / count
    print(f"{key : <20} : {average}")