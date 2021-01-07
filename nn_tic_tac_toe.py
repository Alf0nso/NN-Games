import neural_net as nn
import numpy as np
import utils as ut

# target -> [X,O,D] []
MLP = nn.MLP(9, [40, 20, 10], 3)

p = ut.nn_construct_inpt("tic_games", 3, 3)

targets = []

for target in p[1]:
    x = [0, 0, 0]
    x[int(target)] = 1.0
    targets.append(x)

targets = np.array(targets)
inputs = np.array(p[0])

# print(targets)
# print(inputs)
# input()
# print(np.shape(targets))
# print(np.shape(inputs))

nn.train(MLP, inputs, targets, 40, 0.1)

# print(MLP)
