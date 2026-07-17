# Scenario
# Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.
# Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.
# Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.
# Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.

my_list = []
for i in range(9):
    my_list.append(int(input(f"Enter {i + 1}st number (repition allowed) : ")))

unique_list = []

for number in my_list :
    if number not in unique_list :
        unique_list.append(number)
        
my_list = unique_list
print("\nThe list with unique elements only:")
print(my_list)