# Tic tac toe
#
# Tic tac toe game on python, implementation used
# to learn about neural networks

import os

# Board format should be something like:
#
# (["X","O"," "],[" "," ","O"],[" "," "," "])
#


def clear():
    """
    Simply clears any terminal screen.
    Only meant to make things more readable.
    Should be moved into a separate file
    called "utils"
    """
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


def build_board(r, c):
    """
    Any board that can be represented on a
    tabular manner can be created with this
    function, it's being used here but
    should be changed into a "utils" file.
    """
    return [[" "] * c for i in range(r)]


def print_board(board):
    """
    Prints the board of tic_tac_toe
    can be used to print any game
    state, final result, or just the empty
    board.
    """
    # clear()
    print()
    print("+-" * len(board[0]) + "+")
    for row in board:
        print("", end="|")
        for cell in row:
            print(cell, end="|")
        print()
        print("+-" * len(row) + "+")
    return(0)

# Tic Tac Toe Specific functions
#


def insert_play(board, r, c, symbol, history=None):
    board[r][c] = symbol
    if history is not None:
        history.append([r, c, symbol])
    return 0


def check_if_game_ended(board):
    for line in board:
        if(line[0] == line[1] == line[2]):
            return True
    for column in range(len(board)):
        if(board[0][column] == board[1][column] == board[2][column]):
            return True
    if(board[0][0] == board[1][1] == board[2][2] or
       board[0][2] == board[1][1] == board[2][0]):
        return True
    return False


def play():
    """
    The main cycle of the
    tic_tac_toe game, here all
    the logic will happen with
    it's own passing.
    """
    # A board is created with the respective
    # method, and hostory list is created as
    # well, to save the data of the game
    board = build_board(3, 3)
    history = []
    # Start the game
    while(check_if_game_ended(board)):
        print_board(board)
        print()
        # We are assuming that "X" is the player one
        print("Player 1 (X)")
        print()
        insert_play(board, input("row: "), input("column: "), "X", history)
    return 0
