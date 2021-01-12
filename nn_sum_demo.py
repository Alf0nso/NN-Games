# Demo demonstrating neural network implementation
# learning how to sum two numbers, (exciting I know)
#

import neural_net as nn
import numpy as np
from random import random


mlp = nn.MLP(2, [5], 1)

#  [weights, activations, derivatives]
inputs = np.array([[random() /
                    2 for _ in range(2)]
                   for _ in range(3000)])

target = np.array([[i[0] + i[1]] for i in inputs])
print(target)
print(inputs)
input()

nn.train(mlp, inputs, target, 50, 1)

input = np.array([0.3, 0.2])

output = nn.forward_propagate(input, mlp[0], mlp[1])
print()
print("Prediction of {} + {} is {}".format(
    input[0], input[1], output[0]))
