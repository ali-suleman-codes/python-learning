# Function Parameter Independence
# Purpose:
# Understand that changing a scalar parameter does not affect the original variable.
# Concepts:
# - Function parameters
# - Local scope
# - Scalar arguments

score = 80

def increase_score(score):
    score += 10
    print("Inside function :", score)

increase_score(score)
print("Outside function :", score)