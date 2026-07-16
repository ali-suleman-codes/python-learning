# Scenario
# There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
# Your task is to:
# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
# write a line of code that removes the last element from the list (Step 2)
# write a line of code that prints the length of the existing list (Step 3).

hat_list = [1, 2, 3, 4, 5] 

num = int(input("Enter a number : "))
hat_list[2] = num

del hat_list[-1]

print("Length of list :", len(hat_list))
# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)

