# Weekly Temperature Record

# Purpose:
# Store weekly temperature data in a two-dimensional list and access
# individual weeks and daily temperatures.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# Temperature is recorded for 2 weeks and each week has 7 daily temperatures

temperature = [
    [30, 31, 29, 28, 32, 33, 31],
    [29, 30, 31, 30, 32, 34, 33]
]

print("Week 1 :", temperature[0])
print("Week 2 :", temperature[1])
print("First day of week 2 :", temperature[1][0])
print("Last day of week 1  :", temperature[0][6])