# Neural Network (MLP)
#
# @Author: Afonso Rafael & Renata
#
# Implementation of neural networks in python
# to be used for learning board games. The
# intention is to learn how something like this
# can be written in a programing language

import numpy as np

# The use of the numpy library was to ease
# the burden of some algebra stuff


def MLP(num_inputs=3, hidden_layers=[3, 5], num_outputs=2):

    # Abstract representation of the layers
    layers = [num_inputs] + hidden_layers + [num_outputs]

    weights = []
    for i in range(len(layers) - 1):
        w = np.random.rand(layers[i], layers[i+1])
        weights.append(w)

    derivatives = []
    for i in range(len(layers)-1):
        d = np.zeros((layers[i], layers[i+1]))
        derivatives.append(d)

    activations = []
    for i in range(len(layers)):
        a = np.zeros(layers[i])
        activations.append(a)

    return [weights, activations, derivatives]


def forward_propagate(inputs, weights, activations,
                     derivatives):

    _activations = inputs
    activations[0] = _activations

    for i, w in enumerate(weights):
        net_inputs = np.dot(_activations, w)
        _activations = sigmoid(net_inputs)
        activations[i+1] = _activations

    return _activations


def back_propagate(error, weights, activations,
                   derivatives, verbose=False):

    for i in reversed(range(len(derivatives))):

        _activations = activations[i+1]
        delta = error * sigmoid_derivative(_activations)
        delta_reshaped = delta.reshape(delta.shape[0], -1).T

        current_activations = activations[i]
        current_activations = current_activations.reshape(
            current_activations.shape[0], -1)

        derivatives[i] = np.dot(current_activations,
                                delta_reshaped)

        error = np.dot(delta, weights[i].T)

        if verbose:
            print("W{}: {}".format(i,
                                   derivatives[i]))

    return error


def gradient_descent(weights, derivatives, learning_rate):
    for i in range(len(weights)):
        _weights = weights[i]
        _derivatives = derivatives[i]
        _weights += _derivatives * learning_rate
    pass


def train(mlp, inputs, targets, epochs, learning_rate):

    for i in range(epochs):

        sum_error = 0
        for _input, _target in zip(inputs, targets):

            output = forward_propagate(_input, mlp[0],
                                      mlp[1], mlp[2])

            error = _target - output

            back_propagate(error, mlp[0], mlp[1], mlp[2])

            gradient_descent(mlp[0], mlp[2], learning_rate)

            sum_error += mse(_target, output)

        print("Target: {}, Output: {}"
              .format(_target, output))
        print("Error: {} at epoch {}"
              .format(sum_error / len(inputs), i))
    pass


def mse(target, output):
    return np.average((target - output)**2)


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)

def softmax(x):
    expX = np.exp(x)
    return expX / expX.sum()
