import neural_net as nn

games = open("tic_games", "rt")
#games.readline()

MLP = nn.MLP(9, [200, 125, 75], 3)
