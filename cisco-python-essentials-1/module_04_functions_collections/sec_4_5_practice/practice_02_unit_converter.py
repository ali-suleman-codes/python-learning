# Unit Converter
# Purpose:
# Convert imperial measurements into metric units.
# Concepts:
# - Multiple functions
# - Parameters
# - Default parameter
# - Returning values

def lb_to_kg(lb):
    return lb *  0.45359237

def feet_to_meter(feet, inches = 0.0):
    return feet * 0.3048 + inches * 0.0254

weight = lb_to_kg(120)
height = feet_to_meter(6)
if weight <= 20 or weight >= 200 or \
height <= 1.0 or height >= 2.5 :
    print("Invalid!")
else :
    print("Weight :", weight, "\nHeight :", height)