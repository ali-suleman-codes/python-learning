# Goal

# Ask the user for two integers.

# Display whether:

# first > second
# first < second
# both are equal

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

if num1 == num2 :
    print("Both are equal")
elif num1 > num2 :
    print(num1,"is greater")
else :
    print(num2,"is greater")