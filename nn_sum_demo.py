# Neural Network Demo
#
# @Author: Afonso Rafael & Renata
#
# Demo demonstrating neural network implementation
# learning how to sum two numbers, (exciting I know).
# Can be used to understand how can be used and
# altered to be able to map other functions.

import neural_net as nn
import numpy as np
from random import random

# Libraries necessary to perform the task.

##################################################
mlp = nn.MLP(2, [5], 1)

#  [weights, activations, derivatives]
inputs = np.array([[random() /
                    2 for _ in range(2)]
                   for _ in range(3000)])

target = np.array([[i[0] + i[1]] for i in inputs])

##################################################
print(50*"-")
print("Training The Neural Network!")
print()
nn.train(mlp, inputs, target, 50, 1)


print()
print(50*"-")
print("Testing The Neural Network!")
print()
input = np.array([0.3, 0.2])

output = nn.forward_propagate(input, mlp[0], mlp[1])
print()
print("Prediction of {} + {} is {}".format(
    input[0], input[1], output[0]))
