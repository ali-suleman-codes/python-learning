# Goal
# Input one integer.
# Display:
# Number shifted left by 1
# Number shifted left by 2
# Number shifted right by 1
# Number shifted right by 2

num = int(input("Enter an integer : "))

left_shift = num << 1
print("Number shifted left by 1 :", left_shift)

left_shift = num << 2
print("Number shifted left by 2 :", left_shift)

right_shift = num >> 1
print("Number shifted right by 1 :", right_shift)

right_shift = num >> 2
print("Number shifted right by 2 :", right_shift)