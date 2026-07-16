# Goal
# Input two integers.
# Display the results of all bitwise operations together:
# &
# |
# ^
# <<
# >>
# This acts as a complete revision program for the section.

num1 = int(input("Enter 1st integer : "))
num2 = int(input("Enter 2nd integer : "))

bitwise_and = num1 & num2
bitwise_or = num1 | num2       # 1101
bitwise_xor = num1 ^ num2      # 1001
left_shift = num1 << 2
right_shift = num2 >> 1

print("Result of bitwise AND operation :", bitwise_and)
print("Result of bitwise OR operation :", bitwise_or)
print("Result of bitwise XOR operation :", bitwise_xor)
print("Number shifted left by 2 :", left_shift)
print("Number shifted right by 1 :", right_shift)