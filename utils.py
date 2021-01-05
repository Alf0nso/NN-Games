# Tic tac toe
#
# @Author: Afonso Rafael & Renata
#
# The utils file is just a python file with
# functions that can be/are useful in the
# whole project. Mainly functions related
# with visualization and text editing/processing

import os

# Only the os lib is used mainly to clear
# the screen of the terminal or to write files
# in memory


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


def build_board(r, c, f=" ", t="s"):
    """
    Any board that can be represented on a
    tabular manner can be created with this
    function.
    """
    if t == "i":
        return [[int(f)] * c
                for i in range(r)]
    return [[f] * c for i in range(r)]


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


def check_board(board, char=" ") -> bool:
    """
    check if certain character
    is on the board!
    """

    for row in board:
        if char in row:
            return True
    return False
