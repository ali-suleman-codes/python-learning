"""Practice 1: The Digital Castle Wall
The Concept: Using strict string multiplication and newline spacing to build architectural layout proportions without creating vertical distortion.

The Goal: Output two identical castle towers side-by-side using string multiplication, linked together by a wall.

Expected output :
|__|  |__|    |__|  |__|
|        |====|        |
|________|====|________|  """

print(
    ("|__|  " * 2 ) + "  " + ("|__|  "*2) + "\n" + 
    "|" + " " * 8 + "|" + "====" + "|" + " " * 8 + "|" + "\n" + 
    "|" + "_" * 8 + "|" + "====" + "|" + "_" * 8 + "|"
)