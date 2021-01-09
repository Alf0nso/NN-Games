import utils as ut
import numpy as np
import connect4 as c4
import tic_tac_toe as tic
import games_generator as gg

# generate games
gg.gen_games(tic, 50000, file_name='tic_games')
# gg.gen_games(c4, 10000, file_name='connect4_games')
# tic.play("np")
