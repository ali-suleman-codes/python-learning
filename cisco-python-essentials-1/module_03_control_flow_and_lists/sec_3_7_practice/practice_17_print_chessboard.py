# Chessboard

# Purpose:
# Print a chessboard layout using nested loops.

# Concepts:
# - Nested lists
# - Nested for loops

chess_board = [
    ["R", "K", "B", "Q"],
    ["P", "P", "P", "P"],
    [".", ".", ".", "."]
]

for row in chess_board:
    for chess_piece in row :
        print(chess_piece, end = " ")
    print()