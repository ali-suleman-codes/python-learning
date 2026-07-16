# Goal

# Ask the user for one integer.

# Print its multiplication table from 1 to 10 using a for loop.

num = int(input("Enter a number : "))
for i in range (1, 11):
    print(num, "X", i, "=", num * i)