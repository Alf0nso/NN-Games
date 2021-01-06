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

import numpy as np
import utils as ut
import random


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


def play(game_type='pp'):
    """
    Actual game loop. Each player will be asked to drop their piece.
    If their move is valid, the game proceeds to the other player.
    This cycle will continue until one of the players wins or the
    game ends in a draw.
    A history of the moves and final score will be kept.
    """

    board = ut.build_board(6, 7, f="0", t="i")
    history = []
    game_over = False
    board_full = False
    turn = 0

    while not game_over or board_full:

        if not ut.check_board(board, 0):
            board_full = True
            print('DRAW!')
            history.append('D')

        if turn % 2 == 0:
            # Player 1 plays first and always pair turns
            if game_type == 'pp':
                player1_move = int(input('Player 1 please' +
                                         'choose a number (0,6): '))
            if game_type == 'r':
                player1_move = random.randint(0, 6)

            # if game_type == 'pp_r':
            #   player1_move = NN has to make a prediction
            # if game_type == 'r_nn':
            #   player1_move = random.randint(0, 6)

            if valid_move(board, player1_move):
                row = available_rows(board, player1_move)
                drop_piece(board, row, player1_move, 1)
                history.append([row, player1_move, 1])

                ut.print_board(np.flip(board, 0))

                if win(board, 1):
                    print('PLAYER 1 WINS!')
                    history.append(2)
                    game_over = True
        else:
            # Player 2 plays second and always odd turns
            if game_type == 'pp':
                player2_move = int(input('Player 2 please' +
                                         'choose a number (0,6): '))
            if game_type == 'r':
                player2_move = random.randint(0, 6)
            # if game_type == 'nn_r':
            #   player2_move = random.randint(0, 6)
            # if game_type == 'r_nn':
            #   NN has to make a prediction

            if valid_move(board, player2_move):
                row = available_rows(board, player2_move)
                drop_piece(board, row, player2_move, 2)
                history.append([row, player2_move, 2])

            ut.print_board(np.flip(board, 0))

            if win(board, 2):
                print('PLAYER 2 WINS!')
                history.append(2)
                game_over = True

        turn += 1
    print(history)
    return history
