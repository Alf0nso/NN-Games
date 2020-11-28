# Tic tac toe game generator
#
# @Author: Afonso Rafael

import tic_tac_toe as tic


def gen_tic_tac_toe_games(n_games, path=None,
                          file_name="games"):
    if path is None:
        file_ = open(file_name, "w")
    else:
        file_ = open(str(path) + file_name, "w")

    while(n_games > 0):
        file_.write(str(tic.play("r")))
        file_.write("\n")
        n_games -= 1
    return 0
