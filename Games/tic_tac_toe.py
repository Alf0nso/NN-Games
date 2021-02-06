# Tic tac toe
#
# @Author: Afonso Rafael & Renata
#
# Tic tac toe game on python, implementation used
# to learn about neural networks. It uses generic
# functions built on the 'utils.py' file to generate
# the board, clear the terminal and print characters
# to the screen. The game can be played by two human
# players on the same computer, by random players, or
# by neural networks, or even a combination of all.

from copy import deepcopy
from NN import neural_net as nn
from NN import utils as ut
import numpy as np
import random

# It makes use of the utils library, neural_net,
# numpy and random. deepcopy is used for a list
# copying need.


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
    position = []

    # Encoding player one (X) into the number
    # one, and encoding player two into 2
    if player == 'X':
        enc_play = 1
    else:
        enc_play = 2

    board_temp = deepcopy(board)
    for i, line in enumerate(board_temp):
        for j, cell in enumerate(line):
            if cell == " ":
                board_temp[i][j] = 0

            if cell == "X":
                board_temp[i][j] = 1

            if cell == "O":
                board_temp[i][j] = 2

    for i, line in enumerate(board_temp):
        for j, cell in enumerate(line):
            if cell == 0:

                # Deepcopy is used to avoid instanciating
                # the array!
                _board = deepcopy(board_temp)
                _board[i][j] = enc_play
                possible_p.append(_board)
                position.append([i, j])

    return possible_p, position


def nn_prediction(MLP, board, player):
    """
    Function to compute the prediction of the neural
    network. it will go over all the possibilites and
    save the values, in the end it will only return
    the row and column of the best move.
    """
    stats_player1 = []
    stats_player2 = []

    available_plays, positions = generate_pp(board, player)

    for play, position in zip(available_plays, positions):
        play = np.array(play)
        output = nn.forward_propagate(play.reshape(-1),
                                      MLP[0], MLP[1])
        stats_player1.append(output[0])
        stats_player2.append(output[1])

    if player == "X":
        best_move = stats_player1.index(max(stats_player1))
        row, column = positions[best_move]

    else:
        best_move = stats_player2.index(max(stats_player2))
        row, column = positions[best_move]

    return row+1, column+1


def simulate_games(n_games, nn_file, player1_mode="r", player2_mode="r"):
    """
    Runs more than one game and saves the stats related to that
    game. This can be used to measure how well our neural network
    performs against other neural networks or random players.
    (Or even players if you have the patience to play that many
    games).
    """
    outcomes = []
    while (n_games > 0):
        if nn_file != None:
            history = play(player1_mode, player2_mode, nn_file=nn_file)
        else:
            history = play(player1_mode, player2_mode)
        outcomes.append(history[-1])
        n_games -= 1

    player1_wins = np.sum(
        np.asarray(outcomes) == 'X')/np.sum(
            len(outcomes))*100
    player2_wins = np.sum(
        np.asarray(outcomes) == 'O')/np.sum(
            len(outcomes))*100
    draw = np.sum(np.asarray(outcomes) == 'D')/np.sum(
        len(outcomes))*100

    print('Player 1 Wins:', player1_wins, '%')
    print('Player 2 Wins:', player2_wins, '%')
    print('Draw:', draw, '%')
    pass


def play(player1_mode="r", player2_mode="r",
         nn_file='MLPS/MLP_Tic_Tac_Toe'):
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
    MLP = np.load(nn_file, allow_pickle=True)

    # Start the game
    if (player1_mode == "p" or player2_mode == "p"):
        ut.clear()

    # The game loop
    while(check_if_game_ended(board)[0]):
        if (player1_mode == "p" or player2_mode == "p"):
            print()

        # The Player 1 will always play X
        if (player1_mode == "p" or player2_mode == "p"):
            print("Player 2 (O)" if
                  len(history) % 2 != 0
                  else "Player 1 (X)")

        # Get the input of row and column
        if len(history) % 2 != 0:
            if player2_mode == "p":
                row = int(input("row number: "))
                column = int(input("column number: "))

            elif player2_mode == "r":
                row = random.randint(1, 3)
                column = random.randint(1, 3)

            elif player2_mode == "nn":
                row, column = nn_prediction(MLP, board, "O")

        else:
            if player1_mode == "p":
                row = int(input("row number: "))
                column = int(input("column number: "))

            elif player1_mode == "r":
                row = random.randint(1, 3)
                column = random.randint(1, 3)

            elif player1_mode == "nn":
                row, column = nn_prediction(MLP, board, "X")

        while(True):
            if(row <= 3 and row >= 1 and
               column <= 3 and column >= 1):
                if(board[row - 1][column - 1] != " "):
                    if (player1_mode == "p" or player2_mode == "p"):
                        print("Cell already occupied")
                else:
                    break
            else:
                if (player1_mode == "p" or player2_mode == "p"):
                    print("Cell position does not" +
                          "exist, the board is 3 by 3!")

            if len(history) % 2 != 0:
                if player2_mode == "p":
                    row = int(input("row number: "))
                    column = int(input("column number: "))

                elif player2_mode == "r":
                    row = random.randint(1, 3)
                    column = random.randint(1, 3)

                elif player2_mode == "nn":
                    row, column = nn_prediction(MLP, board, "O")

            else:
                if player1_mode == "p":
                    row = int(input("row number: "))
                    column = int(input("column number: "))

                elif player1_mode == "r":
                    row = random.randint(1, 3)
                    column = random.randint(1, 3)

                elif player1_mode == "nn":
                    row, column = nn_prediction(MLP, board, "X")

        # Insert the play on the board
        insert_play(board, row, column, "O" if
                    len(history) % 2 != 0
                    else "X", history)

        # Print the board only if the game is not
        # between two random players
        if (player1_mode == "p" or player2_mode == "p"):
            ut.print_board(board)

    history.append(check_if_game_ended(board)[1])
    return history
