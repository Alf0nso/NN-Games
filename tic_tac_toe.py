# Tic tac toe
#
# @Author: Afonso Rafael & Renata
#
# Tic tac toe game on python, implementation used
# to learn about neural networks. It uses generic
# functions built on the 'utils.py' file to generate
# the board, clear the terminal and print characters
# to the screen. The game can be played by two human
# players on the same computer.

import utils as ut
import random

# Board format should be something like:
#
# [["X","O"," "],[" "," ","O"],[" "," "," "]]


def insert_play(board, r, c, symbol, history=None):
    board[int(r) - 1][int(c) - 1] = symbol
    if history is not None:
        history.append([r, c, symbol])
    return 0


def check_if_game_ended(board):
    for line in board:
        if(line[0] == line[1] == line[2] == "X"):
            return [False, "X"]
        if(line[0] == line[1] == line[2] == "O"):
            return [False, "O"]
    for column in range(len(board)):
        if(board[0][column] == board[1][column]
           == board[2][column] == "X"):
            return [False, "X"]
        if(board[0][column] == board[1][column]
           == board[2][column] == "O"):
            return [False, "O"]
    if(board[0][0] == board[1][1] == board[2][2] == "X" or
       board[0][2] == board[1][1] == board[2][0] == "X"):
        return [False, "X"]
    if(board[0][0] == board[1][1] == board[2][2] == "O" or
       board[0][2] == board[1][1] == board[2][0] == "O"):
        return [False, "O"]

    for line in board:
        if(" " in line):
            return [True]
    return [False, "D"]


def play(game_type="pp"):
    """
    The main cycle of the
    tic_tac_toe game, here all
    the logic will happen with
    it's own passing.
    """

    # A board is created with the respective
    # method, and history list is created as
    # well, to save the data of the game
    board = ut.build_board(3, 3)
    history = []

    # Start the game
    ut.clear()

    # The game loop
    while(check_if_game_ended(board)[0]):
        print()

        # The Player 1 will always play X
        print("Player 2 (O)" if
              len(history) % 2 != 0
              else "Player 1 (X)")

        print()

        # Get the input of row and column
        if game_type == "pp":
            row = int(input("row number: "))
            column = int(input("column number: "))

        elif game_type == "r":
            row = random.randint(1, 3)
            column = random.randint(1, 3)

        while(True):
            if(row <= 3 and row >= 1 and
               column <= 3 and column >= 1):
                if(board[row - 1][column - 1] != " "):
                    print("Cell already occupied")
                else:
                    break
            else:
                print("Cell position doesn't" +
                      "exist, the board is 3 by 3!")

            if game_type == "pp":
                row = int(input("row number: "))
                column = int(input("column number: "))

            elif game_type == "r":
                row = random.randint(1, 3)
                column = random.randint(1, 3)

        # Insert the play on the board
        #
        insert_play(board, row, column, "O" if
                    len(history) % 2 != 0
                    else "X", history)

        # Print the board
        ut.print_board(board)

    history.append(check_if_game_ended(board)[1])
    return history
