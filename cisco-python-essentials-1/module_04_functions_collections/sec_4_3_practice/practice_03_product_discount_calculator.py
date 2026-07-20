# Product Discount Calculator
# Purpose:
# Practice using returned values inside expressions.
# Concepts:
# - return value
# - Variable assignment
# - Arithmetic operations

def calculate_discount(price):
    discount_rate = 0.21
    return discount_rate * price

price = float(input("Enter price of the product : "))
discount = calculate_discount(price)
final_price = price - discount

print(f"Original price   : {price : .2f}")
print(f"Discount         : {discount : .2f}")
print(f"Discounted price : {final_price : .2f}")


