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


def play():
    """
    The main cycle of the
    tic_tac_toe game, here all
    the logic will happen with
    it's own passing.
    """

    # A board is created with the respective
    # method, and history list is created as
    # well, to save the data of the game
    board = build_board(3, 3)
    history = []

    # Start the game
    clear()

    # The game loop
    while(check_if_game_ended(board)[0]):
        print()

        # The Player 1 will always play X
        print("Player 2 (O)" if
              len(history) % 2 != 0
              else "Player 1 (X)")

        print()

        # Get the input of row and column
        row = int(input("row number: "))
        column = int(input("column number: "))

        while(row > 3 or row < 1
              or column > 3 or column < 1
              or board[row - 1][column - 1] != " "):
            print("Cell " +
                  "already occupied" if board[row - 1][column - 1] != " "
                  else "Row and Column" +
                  "number needs to be between 1 and 3")
            row = int(input("row number: "))
            column = int(input("column number: "))

        # Insert the play on the board
        #
        insert_play(board, row, column, "O" if
                    len(history) % 2 != 0
                    else "X", history)

        # Print the board
        print_board(board)

    history.append(check_if_game_ended(board)[1])
    print(history)
    return 0
