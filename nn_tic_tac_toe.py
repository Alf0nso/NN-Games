import neural_net as nn
import numpy as np
from random import random
import utils as ut

#games = open("tic_games", "rt")
#games.readline()

# target -> [X,O,D] []
MLP = nn.MLP(9, [64, 64], 3)

p = ut.nn_construct_inpt("tic_games", 3, 3)

targets = []

for target in p[1]:
    x = [0, 0, 0]
    x[int(target)] = 1.0
    targets.append(x)

#for target in p[1]:
#    if target == "0":
#        targets.append([0.0])
#    if target == "1":
#        targets.append([0.5])
#    if target == "2":
#        targets.append([1.0])

targets = np.array(targets)
inputs = np.array(p[0])

print(targets)
print(inputs)
input()
print(np.shape(targets))
print(np.shape(inputs))
nn.train(MLP, inputs, targets, 40, 0.1)

print(MLP)
