# Tic tac toe
#
# @Author: Afonso Rafael & Renata
#
# The utils file is just a python file with
# functions that can be/are useful in the
# whole project. Mainly functions related
# with visualization and text editing/processing

import os
import numpy as np
from itertools import chain

# The os lib is used mainly to clear
# the screen of the terminal or to write files
# in memory. Numpy is used because of it's
# math processing power.


def clear():
    """
    Simply clears any terminal screen.
    Only meant to make things more readable.
    """
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')
    pass


def build_board(r, c, f=" ", t="s"):
    """
    Any board that can be represented on a
    tabular manner can be created with this
    function.
    r, c stand for row and column
    f is what we fill in the board with
    t is the type of the thing we use to fill
    the board
    """

    # If type is i then we get an integer
    if t == "i":
        return [[int(f)] * c
                for i in range(r)]

    # If type is f then we get a float
    if t == "f":
        return [[float(f)] * c
                for i in range(r)]

    # Any other type we will get a string
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
    return 0


def check_board(board, char=" ") -> bool:
    """
    check if certain character
    is on the board!
    """
    for row in board:
        if char in row:
            return True
    return False


def nn_construct_input(file, r, c, symbol1='X', symbol2='O', n=0):
    """
    Builds input that is goind to be used to train the
    neural network. it's not the best function, there
    is probably a better way to do this.
    """
    games = open(file, "rt")

    targets = []
    inputs = []
    for line in games:
        line = line[1:-2].replace(
            "'", ""
        ).replace(
            symbol1, "1"
        ).replace(
            symbol2, "2"
        ).replace("D", "3").split(", ")

        games = []
        target = []
        place_holder = []

        for i in range(0, len(line[:-1]), 3):
            if len(place_holder) == 0:
                board = np.zeros((r, c), np.int8)
            else:
                board = np.array(
                    place_holder[-1], np.int8)

            board[int(line[i])-1][int(line[i+1])-1] = int(line[i+2])

            games.append(np.reshape(board, -1))
            place_holder.append(board)
            target.append(line[-1])

        inputs.append(games)
        targets.append(target)

    return [list(chain(*inputs)),
            list(chain(*targets))]
