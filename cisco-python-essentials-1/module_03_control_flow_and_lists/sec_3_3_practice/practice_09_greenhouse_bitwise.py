# Problem Statement
# A computer system stores user permissions inside a single integer called permission_register.
# Each bit represents one permission.
# Bit	Permission
# 0	Read
# 1	Write
# 2	Execute
# 3	Delete
# Your task is to work only with the Delete permission (bit number 3).
# Requirements
# Create
# permission_register = 0
# 1) Create a bit mask for the Delete permission.
# 2) Display the initial value of permission_register.
# 3) Grant the Delete permission.
# 4) Display the updated value.
# 5) Check whether the Delete permission is granted.
# 6) Remove the Delete permission.
# 7)Display the updated value.
# 8) Grant the Delete permission again.
# 9) Toggle (negate) the Delete permission.
# 10) Display the final value.


permission_register = 0
                                              
bit_mask = 8  #1 creates a bit mask 

print("Initial value of permission register :", permission_register) #2 displaying initial value

permission_register |= bit_mask #3 grant delete delete permission

print("Updated value of permission register :", permission_register) #4 displaying updated value

if (permission_register & bit_mask):      #5 displaying permission status
    print("Delete permission is granted")
else :
    print("Delete permission is not granted")  

permission_register &= ~bit_mask  #6 remove delete permission

print("Updated value of permission register :", permission_register) #7 displaying updated value

permission_register |= bit_mask #8 grant delete permission again

permission_register ^= bit_mask  #9 toggle(negate) the delete permission

print("Final value of permission register :", permission_register)   #10 displaying final value