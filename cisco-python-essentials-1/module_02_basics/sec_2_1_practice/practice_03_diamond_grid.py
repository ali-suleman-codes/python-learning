"""
Practice 3: The Symmetrical Diamond Grid
The Concept: Combining exact padding spaces with variable multiplication ratios on a single line to mirror an geometric shape.

The Goal: Build a small diamond, then use string multiplication to render three diamonds horizontally side-by-side. Remember to account for trailing spaces on the right side of the first shape before multiplying!

Expected output : """
#  /\     /\     /\   
# /  \   /  \   /  \  
# \  /   \  /   \  /  
#  \/     \/     \/


print(" /\\    " * 3 + "\n" + 
      "/  \\   " * 3 + "\n" + 
      "\\  /   " * 3 + "\n" + 
      " \\/    " * 3)
