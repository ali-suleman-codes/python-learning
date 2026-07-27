import math

angle_in_degrees = float(input("Enter an angle in degrees : "))
angle_in_radians = math.radians(angle_in_degrees)
print("Angle in radians :", angle_in_radians)
print("sine(", angle_in_degrees, "°) : ", math.sin(angle_in_radians), sep= "")
print("cos(", angle_in_degrees, "°)  : ", math.cos(angle_in_radians), sep= "")
print("tan(", angle_in_degrees, "°)  : ", math.tan(angle_in_radians), sep= "")
