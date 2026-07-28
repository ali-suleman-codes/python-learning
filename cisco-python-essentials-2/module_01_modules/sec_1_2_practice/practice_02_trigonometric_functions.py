import math

angle_in_degrees = float(input("Enter an angle in degrees : "))
angle_in_radians = math.radians(angle_in_degrees)

print("Angle in radians :", angle_in_radians)

print(f"sin({angle_in_degrees})° : {math.sin(angle_in_radians)}")
print(f"cos({angle_in_degrees})° : {math.cos(angle_in_radians)}")
if math.isclose(math.cos(angle_in_radians), 0.0, abs_tol= 1e-12):
    print(f"tan({angle_in_degrees})° : undefined")
else :
    print(f"tan({angle_in_degrees})° : {math.tan(angle_in_radians)}")
