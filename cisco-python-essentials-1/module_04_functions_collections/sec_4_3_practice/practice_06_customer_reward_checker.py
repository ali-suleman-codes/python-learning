# Customer Reward Checker
# Purpose:
# Understand the implicit None returned by functions.
# Concepts:
# - None
# - return
# - if statement

def reward(customer):
    if customer == "premium":
        return "Reward Approved"


customer = "premium"
reward_status = reward(customer)
print(reward_status)

customer = "normal"
reward_status = reward(customer)
print(reward_status)