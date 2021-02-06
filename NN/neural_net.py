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
    """
    Generates the MLP with inputs and outputs and the layers
    specified. The weights are initialised with random values
    """

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

    # Returns the representation of the MLP, which
    # is just a simple array with arrays inside
    return [weights, activations, derivatives]


def forward_propagate(inputs, weights, activations):
    """
    Performes a foward propagation on a MLP, ends
    with the output. The return is the end activations.
    """

    _activations = inputs
    activations[0] = _activations

    for i, w in enumerate(weights):
        net_inputs = np.dot(_activations, w)
        _activations = sigmoid(net_inputs)
        activations[i+1] = _activations

    return _activations


def back_propagate(error, weights, activations,
                   derivatives, verbose=False):
    """
    Picks up the output and the error, with those
    moves backwards and adjusts the weights in order
    to refine the MLP.
    """

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
    # The error is returned
    return error


def gradient_descent(weights, derivatives, learning_rate):
    """
    Goes over all the weights and attempts at moving
    in the direction of the minimum of the function.
    """
    for i in range(len(weights)):
        _weights = weights[i]
        _derivatives = derivatives[i]
        _weights += _derivatives * learning_rate
        weights[i] = _weights
    pass


def train(mlp, inputs, targets, epochs, learning_rate):
    """
    General procedure to train the neural network.
    the amount of times it goes over the data is defined
    by the epochs.
    """

    # The amount of times we will go
    # over the data.
    for i in range(epochs):

        # The overall error that we get
        # with the distance between the
        # MLP guess and the actual value.
        sum_error = 0
        for _input, _target in zip(inputs, targets):

            # [weights, activations, derivatives]
            # foward propagate and get the neural
            # network guess over the data
            output = forward_propagate(_input, mlp[0],
                                       mlp[1])

            # Calculate the difference between
            # the guess and the actual true value
            error = _target - output

            # Propagate the error trought the MLP
            back_propagate(error, mlp[0], mlp[1], mlp[2])

            # Go over the MLP and try to aproximate the
            # the minimum
            gradient_descent(mlp[0], mlp[2], learning_rate)

            # Accumulate the error
            sum_error += mse(_target, output)

        print("Target: {}, Output: {}"
              .format(_target, output))
        print()
        print("Error: {} at epoch {}"
              .format(sum_error / len(inputs), i))
    pass


def mse(target, output):
    """
    Minimum mean square error
    """
    return np.average((target - output)**2)


def sigmoid(x):
    """
    Sigmoid function, logistic function
    """
    return 1.0 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    """
    The derivative of the sigmoid
    function
    """
    return x * (1.0 - x)


def softmax(x):
    """
    The softmax function
    """
    expX = np.exp(x)
    return expX / expX.sum()
