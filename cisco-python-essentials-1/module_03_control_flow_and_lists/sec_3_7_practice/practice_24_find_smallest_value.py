# Find Smallest Value

# Purpose:
# Find the smallest number in a two-dimensional list.

# Concepts:
# - Nested lists
# - Nested loops
# - Comparison

room_temperatures = [
    [31, 28, 33],
    [29, 35, 27],
    [32, 30, 34]
]

smallest_value = room_temperatures[0][0]

for room in room_temperatures :
    for temperature in room:
        if temperature < smallest_value:
            smallest_value = temperature

print("Smallest value :", smallest_value)