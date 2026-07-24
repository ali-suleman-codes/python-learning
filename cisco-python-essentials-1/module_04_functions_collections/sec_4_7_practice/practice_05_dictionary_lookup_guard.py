# Dictionary Lookup Guard

# Purpose:
# Handle missing dictionary keys safely.

# Concepts:
# - Dictionary
# - KeyError
# - try-except

student_information = {}
while True:
    try :
        total_students = int(input("\nHow many students do you want to enter? "))
        if total_students > 0:
            break
        print("Please enter a number greater than 0.")
    except ValueError :
        print("Invalid input : Input must be integer")

for i in range(1, total_students + 1):
    print(f"\nStudent #{i}:")
    name = input("Enter name: ").strip()
    if name != "":
        break
    print("Name cannot be empty.")

    while True:
        try :
            roll_no = int(input(f"\nEnter roll no for {name}: "))
            if roll_no in student_information:
                print("This roll number already exists! Try another one.")
                continue
            break
        except ValueError:
            print("Invalid roll no! Roll number must be an integer")
    student_information[roll_no] = name

while True :
    try :
        num = int(input("\nEnter a roll no : "))
        print("Student name :", student_information[num])
        break
        

    except KeyError:
        print("Invalid key(roll no)! Try another one.")
    except ValueError:
        print("Invalid key(roll no)! Key(roll no) must be an integer.")


