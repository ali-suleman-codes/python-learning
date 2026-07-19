# Arithmetic operators (+, - , /, %, *, **)

a = 5
b = 4
result_sum = a+b
sub= a-b
multiply = a*b
division = a/b
modu = a%b
power = a ** b
print("Sum = ",result_sum)
print("Subtract = ",sub)
print("Multiplication = ",multiply)
print("Division = ",division)   # / operator always give float result
print("Modulus = ",modu)
print(a,"raised to the power ",b," = ",power) # ** is a power operator a**b means a^b

# Relational/Comparison operators (==, !=, >, <, <=, >=)

a = 34
b = 67

print (a == b)
print (a != b)
print (a <= b)
print (a >= b)
print (a < b)
print (a > b)

# Assignment operators (=, +=, -=, /=, *=, %=, **=)

num = 10
print("Num = ",num)
num += 10
print("Num = ",num)
num -= 10
print("Num = ",num)
num *= 10
print("Num = ",num)
num = 10
num **= 10
print("Num = ",num)
num = 10
num %= 10
print("Num = ",num)
num = 10
num /= 10 # always gives floating value
print("Num = ",num)



# Logical operators (and, or, not)
# It works on boolean


a = 6
b = 3
c = False

print(not c )
print (not (a>b))

val1 = True
val2 = False

print("AND Operator : ",val1 and val2)   # False
print("AND Operator : ",(a>b) and (a<b))   # False
print("OR Operator : ",val1 or val2)   # True
print("OR Operator : ",(a>b) or (a<b))   # True

