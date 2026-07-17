# Supermarket Inventory

# Purpose:
# Store product quantities on different shelves.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# A super market has 3 shelves and each shelve has 3 product quantities

inventory_quantity = [
    [15, 20, 18],
    [30, 25, 40],
    [22, 28, 35]
]

print("Shelf 1 :", inventory_quantity[0])
print("Shelf 3 :", inventory_quantity[2])

print("Shelf 2 product 2 quantity :", inventory_quantity[1][1])
print("Shelf 1 product 3 quantity :", inventory_quantity[0][2])