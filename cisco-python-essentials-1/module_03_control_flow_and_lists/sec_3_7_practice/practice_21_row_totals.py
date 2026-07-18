# Row Totals

# Purpose:
# Calculate the total of each row in a two-dimensional list.

# Concepts:
# - Nested lists
# - Nested for loops
# - Accumulator

weekly_sales = [
    [120, 150, 180],
    [140, 160, 190],
    [130, 145, 175]
]

for row_number,branch in enumerate(weekly_sales, start = 1) :
    row_total_sum = 0
    for sale in branch :
        row_total_sum += sale
    print(f"Row {row_number} Total :", row_total_sum)