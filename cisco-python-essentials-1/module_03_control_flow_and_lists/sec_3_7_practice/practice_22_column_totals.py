# Column Totals

# Purpose:
# Calculate the total of each column in a two-dimensional list.

# Concepts:
# - Nested lists
# - Nested for loops
# - Column processing

marks = [
    [78, 82, 91],
    [67, 74, 80],
    [88, 90, 95]
]

column_one_total_sum = 0
column_two_total_sum = 0
column_three_total_sum = 0
for row in marks:
    for index, number in enumerate(row):
        if index == 0 :
            column_one_total_sum += number
        elif index == 1 :
            column_two_total_sum += number
        else :
            column_three_total_sum += number

print("Column 1 Total :", column_one_total_sum)
print("Column 2 Total :", column_two_total_sum)
print("Column 3 Total :", column_three_total_sum)