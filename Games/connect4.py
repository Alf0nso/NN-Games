# Connect 4
#
# @Author: Afonso & Renata
#
# Connect 4 game on python, implementation used
# to learn about neural networks. It uses generic
# functions built on the 'utils.py' file to generate
# the board, clear the terminal and print characters
# to the screen. The game can be played by two human
# players on the same computer.

from copy import deepcopy
import neural_net as nn
import utils as ut
import numpy as np
import random

# Libraries used are basically the same
# ones that where used for tic tac toe.
# Used for similar reasons.


def valid_move(board, col):
    """
    This verifies if the column the players
    choose is empty (== 0) at least in the last
    row (first from the top).
    """
    return board[5][col] == 0


def available_rows(board, col):
    """
    This function returns the next empty row
    in which the new piece will land and the
    player makes his move.
    """
    for row in range(6):
        if board[row][col] == 0:
            return row


def drop_piece(board, row, col, piece):
    """
    This function updates the board.
    It changes the row and column where a piece
    has landed from 0 to the symbol of a player (1 or 2).
    """
    board[row][col] = piece
    return row, col, piece


def win(board, piece):
    """
    Here we assign the rules for winning the game.
    If a player manages to set 4 pieces in a row
    vertically, horizontally or diagonally, they win.
    If there are no winners and the board is full,
    the game ends in a draw.
    """
    # Horizontal
    for col in range(4):
        for row in range(6):
            if board[row][col] == piece and board[row][col+1] == piece and \
                    board[row][col+2] == piece and board[row][col+3] == piece:
                return True
    # Vertical
    for col in range(7):
        for row in range(3):
            if board[row][col] == piece and board[row+1][col] == piece and \
                    board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    # Diagonals (x2 slopes)
    for col in range(4):
        for row in range(3):
            if board[row][col] == piece and board[row+1][col+1] == piece and \
                    board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True
    for col in range(4):
        for row in range(3, 6):
            if board[row][col] == piece and board[row-1][col+1] == piece and \
                    board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True


def generate_pp(board, player):
    """
    Generates the possible next plays.
    can actually be used for a regular player
    but we are only making use of it when
    a neural net is playing.
    """
    possible_p = []
    position = []

    if player == 'R':
        enc_play = 1
    else:
        enc_play = 2

    board_temp = deepcopy(board)
    for i, col in enumerate(board_temp):
        for j, row in enumerate(col):
            if row == 'R':
                board_temp[i][j] = 1
            if row == 'Y':
                board_temp[i][j] = 2

    for i in range(np.shape(board_temp)[1]):
        if valid_move(board_temp, i):
            row = available_rows(board_temp, i)

            # Deepcopy is used to avoid instanciating
            # the array!
            _board = deepcopy(board_temp)
            _board[row][i] = enc_play

            possible_p.append(_board)
            position.append(i)

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

    if player == 'R':
        best_move = stats_player1.index(max(stats_player1))
        column = positions[best_move]

    else:
        best_move = stats_player2.index(max(stats_player2))
        column = positions[best_move]

    return column


def simulate_games(n_games, player1_mode='r', player2_mode='r'):
    """
    Runs more than one game and saves the stats related to that
    game. This can be used to measure how well our neural network
    performs against other neural networks or random players.
    (Or even players if you have the patience to play that many
    games).
    """
    outcomes = []
    while (n_games > 0):
        history = play(player1_mode, player2_mode,
                       nn_file="NN/MLP_Connect4")
        outcomes.append(history[-1])
        n_games -= 1

    player1_wins = np.sum(
        np.asarray(outcomes) == 'R')/np.sum(len(outcomes))*100
    player2_wins = np.sum(
        np.asarray(outcomes) == 'Y')/np.sum(len(outcomes))*100
    draw = np.sum(
        np.asarray(outcomes) == 'D')/np.sum(len(outcomes))*100

    print('Player 1 Wins:', player1_wins, '%')
    print('Player 2 Wins:', player2_wins, '%')
    print('Draw:', draw, '%')
    pass


def play(player1_mode='r', player2_mode='r',
         nn_file='MLP_Connect4'):
    """
    Actual game loop. Each player will be asked
    to drop their piece.
    If their move is valid, the game proceeds
    to the other player.
    This cycle will continue until one of the players
    wins or the game ends in a draw.
    A history of the moves and final score will be kept.
    """

    board = ut.build_board(6, 7, f="0", t="i")
    history = []
    MLP = np.load(nn_file, allow_pickle=True)
    game_over = False
    board_full = False
    turn = 0

    while not (game_over or board_full):

        if turn % 2 == 0:
            # Player 1 plays first and always pair turns
            if player1_mode == 'p':
                player1_move = int(input('Player 1 please' +
                                         ' choose a number (0,6): '))
            elif player1_mode == 'r':
                player1_move = random.randint(0, 6)

            elif player1_mode == "nn":
                player1_move = nn_prediction(MLP, board, "R")

            while not valid_move(board, player1_move):
                if "p" in player1_mode + player2_mode:
                    print("Invalid move! Try again!")
                    print()

                if player1_mode == 'p':
                    player1_move = int(input('Player 1 please' +
                                             'choose a number (0,6): '))
                elif player1_mode == 'r':
                    player1_move = random.randint(0, 6)

                # elif player1_mode == "nn":
                #    player1_move = nn_prediction(MLP, board, "R")

            row = available_rows(board, player1_move)
            drop_piece(board, row, player1_move, 'R')
            history.append([row, player1_move, 'R'])

            if "p" in player1_mode + player2_mode:
                ut.print_board(np.flip(board, 0))

            if win(board, 'R'):
                if "p" in player1_mode + player2_mode:
                    print('PLAYER 1 WINS!')

                history.append('R')
                game_over = True

        else:
            # Player 2 plays second and always odd turns
            if player2_mode == 'p':
                player2_move = int(input('Player 2 please' +
                                         'choose a number (0,6): '))
            elif player2_mode == 'r':
                player2_move = random.randint(0, 6)

            elif player2_mode == "nn":
                player2_move = nn_prediction(MLP, board, "Y")

            while not valid_move(board, player2_move):
                if "p" in player1_mode + player2_mode:
                    print("Invalid move! Try again!")
                    print()

                if player2_mode == 'p':
                    player2_move = int(input('Player 2 please' +
                                             'choose a number (0,6): '))
                elif player2_mode == 'r':
                    player2_move = random.randint(0, 6)

                # elif player2_mode == "nn":
                #    player2_move = nn_prediction(MLP, board, "Y")

            row = available_rows(board, player2_move)
            drop_piece(board, row, player2_move, 'Y')
            history.append([row, player2_move, 'Y'])

            if "p" in player1_mode + player2_mode:
                ut.print_board(np.flip(board, 0))

            if win(board, 'Y'):
                if "p" in player1_mode + player2_mode:
                    print('PLAYER 2 WINS!')
                history.append('Y')
                game_over = True

        if 0 not in board[5] and not game_over:
            board_full = True
            if "p" in player1_mode + player2_mode:
                print('DRAW!')
            history.append('D')

        turn += 1

    return history
