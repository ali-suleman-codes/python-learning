import math

number = float(input("Enter a number : "))


print(f"atan({number}) : {math.degrees(math.atan(number))}°")

if -1 <= number <= 1:
    print(f"acos({number}) : {math.degrees(math.acos(number))}°")
    print(f"asin({number}) : {math.degrees(math.asin(number))}°")
else :
    print(f"asin({number}) : out of domain")
    print(f"acos({number}) : out of domain")


print()
print(f"sinh({number}) : {math.sinh(number)}")
print(f"cosh({number}) : {math.cosh(number)}")
print(f"tanh({number}) : {math.tanh(number)}")

