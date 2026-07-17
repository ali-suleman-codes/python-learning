# Computer Lab

# Purpose:
# Store computer numbers row-wise in a computer lab.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# A computer lab has 3 rows and each row has 4 computers

computer_lab_grid = [
    ["PC01", "PC02", "PC03", "PC04"],
    ["PC05", "PC06", "PC07", "PC08"],
    ["PC09", "PC10", "PC11", "PC12"]
]

print("Row 2         :", computer_lab_grid[1])

print("Computer 03   :", computer_lab_grid[0][2])
print("Computer 10   :", computer_lab_grid[2][1])
print("Last computer :", computer_lab_grid[2][3])