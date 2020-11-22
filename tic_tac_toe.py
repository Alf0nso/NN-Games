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
    return [[" "] * c] * r


def print_board(board):
    """
    Prints the board of tic_tac_toe
    can be used to print any game
    state, final result, or just the empty
    board.
    """
    # clear()
    print()
    print(" _ _ _ ")
    for row in board:
        print("", end="|")
        for cell in row:
            print(cell, end="|")
        print("\n")
    return(0)



def play():
    """
    The main cycle of the
    tic_tac_toe game, here all
    the logic will happen with
    it's own passing.
    """
    # A board is created with the respective
    # method
    board = build_board()
    print_board(board)
    return 0
