"""
Practice 5: The Horizontal Loading Bar
The Concepts: The end= keyword to keep multiple print() statements on the same line, combined with string multiplication.

The Goal: Build a loading bar that prints its pieces sequentially without jumping to a new line, ending with a "100%" message.

Expected output :
Loading: [==========] 100% Complete! 
"""

print("Loading:", end = " ")
print("[" + "=" * 10 + "]", end = " ")
print("100%", end = " ")
print("Complete!") 