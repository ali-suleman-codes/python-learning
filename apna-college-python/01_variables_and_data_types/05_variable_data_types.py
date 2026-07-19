# We don't need semicolon in python just write print() which is a function and what you
# write in the paranthesis will be printed.

print ("Ali","Suleman")
print (25,56)
print ("UON")
print (25+67)

# To write in the same line we use comma (,) and to write in next line we simply use next 
# print() function

# We simply name variable without writing data type

name = "Ali"
age = 23
price = 45.34
print(name,age,price)
print("My name is  ",name,"My age is  ",age,"Price of football is  ",price)

age2 = age
print(age2)

#  We can check the type of variable by using type() function

print(type(name))
print(type(age))
print(type(price))

# We can write string in single, double, triple quotes but for consistency we use double quotes

name1 = 'Ali1'
name2 = "Ali2"
name3 = '''Ali3'''
print(name1,name2,name3)

"""
We use # for single line comments and triple quotes  for multi-line comments
There are 5 basic built-in primitive data types in python 1) int 2) float 3) string 4) bool 5) None
"""

age3 = 23
old = True
a = None

# True, False, None is valid but true, false, none gives error
# None means we don't give any value to variables

print(age3)
print(old)
print(a)

print(type(age3))
print(type(old))
print(type(a))