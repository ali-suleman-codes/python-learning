# =====================================================================
# Project : Tic-Tac-Toe Game
# Course  : Python Essentials 1
# Module  : Module 04 - Functions, Tuples, Dictionaries and Exceptions
# Author  : Muhammad Ali Suleman Rajpoot
# Date    : 24-25 July 2026
#
# Description:
#   A console-based Tic-Tac-Toe game where:
#     - The player uses O and the computer uses X.
#     - The computer starts with the center square occupied.
#     - The player enters moves using numbers 1-9.
#     - The computer selects random valid moves.
#     - The program checks for wins and draws.
#     - Invalid input is handled using exception handling.
# =====================================================================
import sys
from random import randrange

board = [[ "1", "2", "3"],
         [ "4", "X", "6"],
         [ "7", "8", "9"]
]

# # The function clears the terminal
# def clear_terminal():
#     sys.stdout.write("\033[2J\033[H")
#     sys.stdout.flush()

# The function checks the valid move of the user.
def check_move() :
    min_move = 1
    max_move = 9
    while True:
        try :
            entered_move = int(input("\nEnter your move: "))
            if entered_move < min_move or entered_move > max_move:
                print("Invalid Input! Please enter an integer (1-9).")
            else :
                return entered_move
        except ValueError:
            print("Invalid Input! Please enter  an integer(1-9).")



# The function accepts one parameter containing the board's current status
# and prints it out to the console.
def display_board(board):
    for row in board:
        print(("+" + "-" * 7) * 3 + "+")
        print(("|" + " " * 7) * 3 + "|")
        for i in row:
            print("|" + " " * 3, end = "")
            print(i + " " * 3, end = "")
        print("|")
        print(("|" + " " * 7) * 3 + "|")

    print(("+" + "-" * 7) * 3 + "+")

# the list consists of tuples, while each tuple is a pair of row and column numbers.
# The function browses the board and builds a list of all the free squares; 
def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "O" and board[i][j] != "X":
                free_fields.append((i, j))
    return free_fields


# The function accepts the board's current status, asks the user about their move, 
# checks the input, and updates the board according to the user's decision.
def enter_move(board):
    while True:
        move = str(check_move())
        free_fields = make_list_of_free_fields(board)
        for i, j in free_fields:
            if board[i][j] == move:
                board[i][j] = "O"
                return
            
        print("Invalid Move! Please enter correct move.")
            


# The function analyzes the board's status in order to check if 
# the player using 'O's or 'X's has won the game
def victory_for(board, sign):
    
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True

        elif board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    
    return False
    

# The function draws the computer's move and updates the board.
def draw_move(board):
    board_free_fields = make_list_of_free_fields(board)
    random_move = randrange(len(board_free_fields))
    pair = board_free_fields[random_move]
    board[pair[0]][pair[1]]= "X"

def main():
    display_board(board)                       # Display initial board status
    while True:
        enter_move(board)                      # Read move from user
        display_board(board)                   # Display board status after user move
        if victory_for(board, "O"):            # Check user winning status
            print("You won!")
            break
        draw_move(board)                       # Play computer move
        display_board(board)                   # Display board status after computer move
        if victory_for(board, "X"):            # Check computer winning status
            print("Computer won!")
            break
        if not make_list_of_free_fields(board):
            print("Games end with a tie!")
            break

if __name__ == "__main__":
    try :
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting safely... Goodbye!")