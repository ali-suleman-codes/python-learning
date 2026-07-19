#  1) Write a program to input 2 numbers and print their sum

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
result_sum = num1 + num2
print("Sum = ",result_sum)

# 2) Write a program to input side of a square and print its area

side = float(input("Enter side of a square :"))
# area = side * side  or 
area = side **2
print("Area = ",area)

# 3) Write a program to input two floating numbers and print their average

num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))
average = (num1 + num2)/2
print("Average = ",average)

# Write a program to input two numbers, a and b. Print True if a is greater than or
# or equal to b. If not, print False

a = int(input("Enter a:"))
b = int(input("Enter b:"))
print(a>=b)
