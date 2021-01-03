import games_generator as gg
import connect4
import tic_tac_toe as tic

# generate games
gg.gen_games(tic, 10, file_name='tic_games')
gg.gen_games(connect4, 10, file_name='connect4_games')
