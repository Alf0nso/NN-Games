# Tic tac toe
#
# @Author: Afonso Rafael & Renata
#
# Train the neural network on
# connect4 games and observe how it
# performs!

import neural_net as nn
import numpy as np
import utils as ut
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

# libraries both for making the MLP and
# for testing it.

print()
print(50*"-")
print("Generating Neural Net")
MLP = np.array(nn.MLP(42, [15, 10], 3), dtype='object')

p = ut.nn_construct_input("connect4_games", 6, 7, 'R', 'Y')
targets = []

for target in p[1]:
    x = [0, 0, 0]
    x[int(target) - 1] = 1.0
    targets.append(x)

targets = np.array(targets)
inputs = np.array(p[0])


# Spliting the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(inputs, targets, test_size=0.2, random_state=42, stratify=targets)

print()
print(50*"-")
print("Training The Neural Neural Network")
nn.train(MLP, X_train, y_train, 25, 0.1)

print(50*"-")
print("Testing the Neural Network")

outputs = nn.forward_propagate(X_test, MLP[0], MLP[1])

print()
print()

pred_y = []
for output in outputs:
    output = list(output)
    pred_labels = [0, 0, 0]
    pred_labels[output.index(max(output))] = 1.0
    pred_y.append(pred_labels)


print('Accuracy for Testing Set: ',
      accuracy_score(y_test, np.array(pred_y)))
print('F1 Score for Testing Set: ',
      f1_score(y_test, np.array(pred_y), average='weighted'))

# file = open("Connect4_2_attempt", "wb")
# np.save(file, MLP)
# file.close
