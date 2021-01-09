import neural_net as nn
import numpy as np
import utils as ut

print()
print(50*"-")
print("Generating Neural Net")
MLP = np.array(nn.MLP(9, [27, 27, 27], 3), dtype='object')

p = ut.nn_construct_inpt("tic_games", 3, 3)
targets = []

for target in p[1]:
    x = [0, 0, 0]
    x[int(target) - 1] = 1.0
    targets.append(x)

targets = np.array(targets)
inputs = np.array(p[0])

#print()
#print(50*"-")
#print("Training The Neural Neural Network")
#nn.train(MLP, inputs, targets, 5, 0.1)
#
#
#print(50*"-")
#print("Testing the Neural Network")
#test = np.array([1, 2, 1, 2, 1, 0, 2, 0, 0])
#
#output = nn.forward_propagate(test, MLP[0], MLP[1], MLP[2])
#
#print()
#print(output)
#
#file = open("Neural_Network", "wb")
#np.save(file, MLP)
#file.close
