# Even Number List Creator
# Purpose:
# Learn how a function can return a list.
# Concepts:
# - Lists
# - return
# - range()

def even_list(limit):
    even = []
    for i in range(1,limit + 1):
        if i % 2 == 0:
            even.append(i)
    
    return even

limit = int(input("Enter a number : "))
even_numbers = even_list(limit)

print(even_numbers)




