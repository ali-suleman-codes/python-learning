# Student Grade Evaluation
# Purpose:
# Understand that a function can return early without completing the remaining statements.
# Concepts:
# - return without expression
# - Function termination
# - if statement

def result(attendance):
    if attendance == "absent" :
        return
    else :
        print("Student Result : Passed")

attendance_status = "absent"
result(attendance_status) # nothing will print
attendance_status = "present"
result(attendance_status) # display result message



