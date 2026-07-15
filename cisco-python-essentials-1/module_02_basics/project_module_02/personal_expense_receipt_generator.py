# ==========================================================
# Project : Personal Expense Receipt Generator
# Module  : Python Essentials 1 - Module 02 Milestone Project
# Author  : Muhammad Ali Suleman Rajpoot
# Date    : 15 July 2026
# Description:
#     Generates a shopping receipt for three products,
#     calculates subtotal, tax, and grand total.
# ==========================================================

shop_name = input("Enter shop name : ")
customer_name = input("Enter customer name : ")

print("\nEnter product 1 details")
product_one_name = input("Enter product name : ")
product_one_price = float(input("Enter product price : "))
product_one_quantity = int(input("Enter quantity : "))

print("\nEnter product 2 details")
product_two_name = input("Enter product name : ")
product_two_price = float(input("Enter product price : "))
product_two_quantity = int(input("Enter quantity : "))

print("\nEnter product 3 details")
product_three_name = input("Enter product name : ")
product_three_price = float(input("Enter product price : "))
product_three_quantity = int(input("Enter quantity : "))

product_one_total = product_one_quantity * product_one_price
product_two_total = product_two_quantity * product_two_price
product_three_total = product_three_quantity * product_three_price

sub_total = product_one_total + product_two_total + product_three_total
tax = sub_total * 10 / 100 # suppose tax is 10 %
grand_total = sub_total + tax

print("=" * 40)
print("\t", shop_name)
print("=" * 40, "\n")

print("-" * 40)
print("Customer :", customer_name)
print("-" * 40)


print("-" * 40)
print("Product 1 ")
print("Product name :", product_one_name)
print("Price        :", product_one_price)
print("Quantity     :", product_one_quantity)
print("Total        :", product_one_total)
print("-" * 40)

print("-" * 40)
print("Product 2  ")
print("Product name :", product_two_name)
print("Price        :", product_two_price)
print("Quantity     :", product_two_quantity)
print("Total        :", product_two_total)
print("-" * 40)

print("-" * 40)
print("Product 3 ")
print("Product name :", product_three_name)
print("Price        :", product_three_price)
print("Quantity     :", product_three_quantity)
print("Total        :", product_three_total)
print("-" * 40)

print("-" * 40)
print("Receipt no.  : 1234")
print("Tax rate     : 10%")
print("Subtotal     :", sub_total)
print("Tax          :", tax)
print("-" * 40)

print("Grand Total  :", grand_total)
print("=" * 40)

print("Thank you for shopping!")