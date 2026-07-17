# Statement
# A warehouse stores five package weights.
# [25, 10, 40, 15, 30]
# Perform only one complete pass of Bubble Sort.
# Print the list before and after the pass.

my_list = [25, 10, 40, 15, 30]
print("Original :", my_list)

for i in range(0, len(my_list) - 1) :
    if my_list[i] > my_list[i + 1]:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    
print("After one pass :", my_list)