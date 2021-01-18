# Tic tac toe
#
# @Author: Afonso Rafael & Renata
#
# Game generator. Functions related to
# generating various amounts of games to
# train the neural networks.

from itertools import chain

# Chain is used to produce the strings
# that are saved in the file


def gen_games(game, n_games, path=None,
              file_name="games"):
    """
    Generates files of games of any kind. What
    writes onto the files is the final result
    that is given by the play() function, and
    the history that comes with it.
    """

    if path is None:
        file_ = open(file_name, "w")
    else:
        file_ = open(str(path) + file_name, "w")

    while(n_games > 0):
        file_.write(str(list(chain(
            *game.play(player1_mode='r', player2_mode='r')))))
        file_.write("\n")
        n_games -= 1
    return 0
