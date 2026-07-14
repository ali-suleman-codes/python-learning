"""Scenario : 
The print() command, which is one of the easiest directives in Python, simply prints out a line to the screen.

In your first lab:

1) Use the print() function to print the line Hello, Python! to the screen. Use double quotes around the string.
2) Having done that, use the print() function again, but this time print your first name.
3) Remove the double quotes and run your code. Watch Python's reaction. What kind of error is thrown?
4) Then, remove the parentheses, put back the double quotes, and run your code again. What kind of error is thrown this time?
5) Experiment as much as you can. Change double quotes to single quotes, use multiple print() functions on the same line, and then on different lines. See what happens."""

print("Hello, python!") # Hello, python

print("Ali") # Ali

# print(Ali) # This will throw NameError

# print "Ali" # This will syntaxError

print('Ali Suleman') # Python allows to use single, double and triple quotes for a string
# print("Hello, python!") print("Ali") # Python doesn't allow to write multiple print() in one line, it will throw syntaxError
