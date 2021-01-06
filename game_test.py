from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential
from keras.utils import to_categorical
import numpy as np
import utils as ut


class TicTacToeModel:

    def __init__(self, numberOfInputs, numberOfOutputs, epochs, batchSize):
        self.epochs = epochs
        self.batchSize = batchSize
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_shape=(numberOfInputs, )))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(numberOfOutputs, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    def train(self, input, output):
        input = []
        output = []
        for data in dataset:
            input.append(data[0])
            output.append(data[1])

        X = np.array(input).reshape((-1, self.numberOfInputs))
        y = output
        # Train and test data split
        boundary = int(0.8 * len(X))
        X_train = X[:boundary]
        X_test = X[boundary:]
        y_train = y[:boundary]
        y_test = y[boundary:]

        self.model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=self.epochs, batch_size=self.batchSize)

    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs))[0][index]

if __name__ == "__main__":

    p = ut.nn_construct_inpt("tic_games", 3, 3)

    targets = []

    for target in p[1]:
        #x = [0, 0, 0]
        #x[int(target)] = 1.0
        #targets.append(x)

    targets = np.array(targets)
    inputs = np.array(p[0])

    ticTacToeModel = TicTacToeModel(9, 3, 100, 12)
    ticTacToeModel.train(inputs, targets)
