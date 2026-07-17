# Chessboard Positions

# Purpose:
# Represent a chessboard using a nested list and retrieve
# specific board positions.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

chess_board = [
    ["Rook", "Knight", "Bishop", "Queen"],
    ["Pawn1", "Pawn2", "Pawn3", "Pawn4"],
    ["Empty1", "Empty2", "Empty3", "Empty4"]
]

print("Queen             :", chess_board[0][3])
print("First Pawn        :", chess_board[1][0])
print("Last empty square :", chess_board[2][3])