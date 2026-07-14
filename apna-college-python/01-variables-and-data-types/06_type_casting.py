# Type conversion

a=2
b=4.5

sum = a+b
print("Sum = ",sum)

# Type casting

# 1) String to int

c = int("2")   # Only work with string when it has convertable value not work with text
d = 3.6
multi = c * d
print("Multiplication = ",multi)

e = "3"
print(type(e))
e = int("3")
print(e)
print(type(e))

# 2) Float to int
f =5.5
g = int(f)
print(g)
print(type(g))

# 3) Int to float
h =5
i = float(h)
print(i)
print(type(i))

# 4) bool to int/float

j = False
k = float(j)
print(k)
print(type(k))

# l = None
# m = int(l)
# print(m)
# print(type(m))

# throws error because type casting works
# with string which has an integer or float
# and with number like 1, 0, float, int