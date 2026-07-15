# Problem Statement

# Ask the user to enter:

# Product name
# Price
# Quantity

# Calculate:

# Total price

# Display a formatted shopping receipt.

product_name = input("Enter product name : ")
price = float(input("Enter price of product : "))
quantity = int(input("Enter quantity : "))

total_price = price * quantity

print("+" + "-" * 30 + "+")
print("\tSHOPPING RECEIPT")
print("Product name        :", product_name)
print("Product price       :", price)
print("Quantity of product :", quantity)
print("Total price         :", total_price)
print("+" + "-" * 30 + "+")