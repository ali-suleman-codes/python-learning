# List Index Guard

# Purpose:
# Handle invalid list indexing.

# Concepts:
# - Lists
# - IndexError
# - try-except

seat_number = [1, 2, 3, 4, 5]

while True:
    try :
        index = int(input("\nEnter index : "))
        print("Seat number :", seat_number[index])
        break
    except IndexError:
        print("Invalid index! Try another one.")
    except ValueError:
        print("Invalid index! Index must be an integer.")
    