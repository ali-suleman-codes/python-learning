# Hotel Room Prices

# Purpose:
# Store room prices floor-wise using a nested list.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# A building has 3 floors and 3 rooms

floor_room_prices = [
    [4500, 5000, 5500],
    [6000, 6500, 7000],
    [7500, 8000, 8500]
]
print("Floor 2 prices :", floor_room_prices[1])

print("Cheapes room price :", floor_room_prices[0][0])

print("Expensive room price :", floor_room_prices[2][2])