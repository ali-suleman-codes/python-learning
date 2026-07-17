#  Statement
# A shop stores monthly sales.
# [120, 150, 130, 170, 160, 180]
# Print
# first three months
# last three months
# highest sale (without using `max()`)
# whether 170 exists in the list

monthly_sales = [120, 150, 130, 170, 160, 180]

first_three_months = monthly_sales[: 3]
last_three_months = monthly_sales[-3 :]

print("First three months :", first_three_months)
print("Last three months  :", last_three_months)

highest_sale = monthly_sales[0]

for i in monthly_sales:
    if i > highest_sale :
        highest_sale =  i

print("Highest sale       :", highest_sale)

if 170 in monthly_sales :
    print(170, "exists in the list")