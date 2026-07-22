# Fibonacci Number Generator
# Purpose:
# Calculate the nth Fibonacci number.
# Concepts:
# - Variables
# - for loop
# - return

def fibonacii(num):
    if num < 1:
        return None
    if num < 3:
        return 1
    elem1 = elem2 = 1
    my_sum = 0
    for i in range(3, num + 1):
        my_sum = elem1 + elem2
        elem1, elem2 = elem2, my_sum

    return my_sum

print("9th Fibonacci Number :", fibonacii(9))