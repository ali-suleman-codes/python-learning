# ===============================================================
# Project : Smart Student Gradebook
# Course  : Python Essentials 1 
# Module  : Module 03 - Lists
# Author  : Muhammad Ali Suleman Rajpoot
# Date    : 18-19 July 2026
# Description:
#   A console-based student grade management system.
#     - Stores student names and marks using nested lists.
#     - Displays student records in tabular format.
#     - Calculates totals, averages, grades and class average.
#     - Finds topper, lowest scorer and subject toppers.
#     - Counts passed and failed students.
#     - Searches student records by name.
# ===============================================================

import sys

# Display the application heading.

print("=" * 46)
print("|🎊🎊 WELCOME TO SMART STUDENT GRADEBOOK 🎊🎊|")
print("=" * 46)

print("\n🚀Launching the app..\n")

# Read the number of students from the teacher.

student_number = int(input("How many students❓ : "))

if student_number <= 0 :
    print("\nNumber of students must be greater than zero.")
    sys.exit()

student_matrix = []   # Store the details of all students.

# Collect each student's information.

for i in range(student_number) :
    student_list = [] # Store one student's information.
    input(f"\nPress Enter to fill the details of student {i + 1} : ")

    # Read the student's name and subject marks.

    student_list.append(input("Enter name of the student : "))
    student_list.append(int(input("Enter Math marks : ")))
    student_list.append(int(input("Enter English marks : ")))
    student_list.append(int(input("Enter Computer marks : ")))

    student_matrix.append(student_list) # Add the student's record to the gradebook.

# Define column indexes.

NAME = 0
MATH = 1
ENGLISH = 2
COMPUTER = 3
TOTAL_SUBJECTS = 3

# Calculate the required column width for table formatting.

max_name_length = max( len(row[NAME]) for row in student_matrix)
col_width = max_name_length + 4

# Display all student records.

print()
print("=" * (col_width + 35))
print(f"{'Name' : <{col_width}} {'Math' : <10} {'English' : <10} {'Computer' : <10}")
print("-" * (col_width + 35))

for row in student_matrix :
    print(f"{row[NAME] : <{col_width}} {row[MATH] : <10} {row[ENGLISH] : <10} {row[COMPUTER] : <10}")

print("=" * (col_width + 35))
print()

average_marks = [] # Store each student's average marks.
class_total_marks = 0    # Store the total marks of the entire class.

# Process each student's record.

for row in student_matrix :
    total_marks = 0  # Calculate the total marks for the current student.

# Add marks of all subjects.

    for marks in row[1 : ] : 
        total_marks += marks
    print(f"Total marks of {row[NAME]}   : {total_marks}")

    average = total_marks / TOTAL_SUBJECTS
    print(f"Average marks of {row[NAME]} : {average : .2f}") # Display the average with 2 decimal places.
    print()

    class_total_marks += total_marks

    average_marks.append(average)

highest_score = average_marks[0]

# Find the highest average.

for marks in average_marks :
    if marks > highest_score :
        highest_score = marks

# Find the topper's index.

topper_index = 0

for i in range(student_number) :
    if highest_score == average_marks[i]:
        topper_index = i
        break
print("\nHighest scorer :", student_matrix[topper_index][NAME])

# Find the lowest average.

lowest_score = average_marks[0]
for marks in average_marks :
    if marks < lowest_score :
        lowest_score = marks

# Find the lowest scorer's index.

lowest_index = 0

for i in range(student_number) :
    if lowest_score == average_marks[i]:
        lowest_index = i
        break
print("Lowest scorer  :", student_matrix[lowest_index][NAME])

# Find the highest Mathematics marks. 
 
highest_math_marks = student_matrix[NAME][MATH]
for i in range(student_number):
    if student_matrix[i][MATH] > highest_math_marks:
        highest_math_marks = student_matrix[i][MATH]

# Find the highest English marks.

highest_eng_marks = student_matrix[NAME][ENGLISH]
for i in range(student_number):
    if student_matrix[i][ENGLISH] > highest_eng_marks:
        highest_eng_marks = student_matrix[i][ENGLISH]

# Find the highest Computer marks.

highest_com_marks = student_matrix[NAME][COMPUTER]
for i in range(student_number):
    if student_matrix[i][COMPUTER] > highest_com_marks:
        highest_com_marks = student_matrix[i][COMPUTER]

# Display the highest marks in each subject.

print("\nHighest Math marks     :", highest_math_marks)
print("Highest English marks  :", highest_eng_marks)
print("Highest Computer marks :", highest_com_marks)

# Search for a student by name.

found_name = False

search_student_name = input("\nEnter student name : ").lower() # Convert the input to lowercase for case insensitive searching.
for i in range(student_number):
    if search_student_name == student_matrix[i][NAME].lower():
        found_name = True
        break 

# Display the student's marks.

if found_name :
    print("\nName           :", student_matrix[i][NAME])
    print("Math marks     :", student_matrix[i][MATH])
    print("English marks  :", student_matrix[i][ENGLISH])
    print("Computer marks :", student_matrix[i][COMPUTER])
else :
    print("Student not found") # Display the message if student not found.

# Count passed and failed students.

counter_failed = 0

for row in student_matrix :
    for marks in row[1 : ]:
        if marks < 40 :
            counter_failed += 1
            break

# Display the number of passed and failed students.

print("\nTotal passed students :", student_number - counter_failed)
print("Total failed students :", counter_failed)

# Calculate the class average.

class_average = class_total_marks / (student_number * TOTAL_SUBJECTS)
print(f"\nClass Average : {class_average : .2f}")

# Display the class topper.

print("\nTopper :", student_matrix[topper_index][NAME])
print()

# Display the grade of each student. 

print(f"{'\nName' : <{col_width}}  Grade")
for i in range(student_number):

    if average_marks[i] >= 90 :
        print(f"{student_matrix[i][NAME] : <{col_width}} : A+")
    elif average_marks[i] >= 80 :
        print(f"{student_matrix[i][NAME] : <{col_width}} : A")

    elif average_marks[i] >= 70 :
        print(f"{student_matrix[i][NAME] : <{col_width}} : B")

    elif average_marks[i] >= 60 :
        print(f"{student_matrix[i][NAME] : <{col_width}} : C")

    else :
        print(f"{student_matrix[i][NAME] : <{col_width}} : F")
