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

import neural_net as nn
import utils as ut
import numpy as np
import random

# Board format should be something like:
#
# [["X","O"," "],[" "," ","O"],[" "," "," "]]


def insert_play(board, r, c, symbol, history=None):
    """
    Function to insert moves on the board.
    """
    board[int(r) - 1][int(c) - 1] = symbol
    if history is not None:
        history.append([r, c, symbol])
    pass


def check_if_game_ended(board):
    """
    Check if the game as already finished
    and return who won, or if it was a draw
    """
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


def generate_pp(board, player):
    """
    Generates the possible next plays.
    can actually be used for a regular player
    but we are only making use of it when
    a neural net is playing.
    """
    possible_p = []

    for i, line in enumerate(board):
        for j, el in enumerate(line):
            if el == " ":
                _board = board
                _board[i][j] = player
                possible_p.append(_board)

    return possible_p


def nn_prediction(MLP, Plays):
    output = nn.forward_propagate(
        input, MLP[0], MLP[1], MLP[2])

    return output


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
    MLP = None

    # Start the game
    if game_type != "rr":
        ut.clear()

    # Generate a neura network and train it!
    if game_type == "np" or game_type == "pn":
        print(50*"-")
        print("Generating a Neural Network")

        # Creating  a multy layer perceptron
        MLP = nn.MLP(9, [40, 20, 10], 3)

        # Getting the data from the
        # tic_games file
        feed_data = ut.nn_construct_inpt(
            "tic_games", 3, 3)

        targets = []

        for target in feed_data[1]:
            x = [0, 0, 0]
            x[int(target)] = 1.0
            targets.append(x)

        inputs = np.array(feed_data[0])
        targets = np.array(targets)
        print()
        print("training")
        nn.train(MLP, inputs, targets, 40, 0.1)
        print()
        print(50*"-")
        print("finished training!")
        print(50*"-")

    # The game loop
    while(check_if_game_ended(board)[0]):
        if game_type != "rr":
            print()

        # The Player 1 will always play X
        if game_type != "rr":
            print("Player 2 (O)" if
                  len(history) % 2 != 0
                  else "Player 1 (X)")

        # Get the input of row and column
        if game_type == "pp":
            row = int(input("row number: "))
            column = int(input("column number: "))

        elif game_type == "rr":
            row = random.randint(1, 3)
            column = random.randint(1, 3)

        elif game_type == "np":
            if len(history) % 2 != 0:
                p = generate_pp(board, "X")
                print(p)
                input()
                break
            pass

        while(True):
            if(row <= 3 and row >= 1 and
               column <= 3 and column >= 1):
                if(board[row - 1][column - 1] != " "):
                    if game_type != "rr":
                        print("Cell already occupied")
                else:
                    break
            else:
                if game_type != "rr":
                    print("Cell position doesn't" +
                          "exist, the board is 3 by 3!")

            if game_type == "pp":
                row = int(input("row number: "))
                column = int(input("column number: "))

            elif game_type == "rr":
                row = random.randint(1, 3)
                column = random.randint(1, 3)

        # Insert the play on the board
        insert_play(board, row, column, "O" if
                    len(history) % 2 != 0
                    else "X", history)

        # Print the board only if the game is not
        # between two random players
        if game_type != "rr":
            ut.print_board(board)

    history.append(check_if_game_ended(board)[1])
    return history
