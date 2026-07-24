# Default Exception Demonstrator

# Purpose:
# Understand how a default except block works.

# Concepts:
# - try
# - except
# - Exception handling

try :
    student_tuple = (1, 2, 3, 4)
    student_tuple[0] = student_tuple[1] + student_tuple[2]

except Exception :
    print("Tuples are immutable")