# Scenario
# Your task is to complete the code in order to evaluate the expression.
# The result should be assigned to y. Be careful ‒ watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.

x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

print("y =", y)
