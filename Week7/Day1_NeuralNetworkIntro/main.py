# Week 7 - Day 1 - Introduction to Neural Networks
# A neuron takes inputs, multiplies by weights, adds bias,
# and passes the result through an activation function.

import numpy as np

inputs = np.array([2.0, 3.0])
weights = np.array([0.5, -0.2])
bias = 0.1

weighted_sum = np.dot(inputs, weights) + bias
relu_output = max(0, weighted_sum)

print("Inputs:", inputs)
print("Weights:", weights)
print("Bias:", bias)
print("Weighted sum:", round(weighted_sum, 2))
print("ReLU activation output:", round(relu_output, 2))
print("\nNeural networks combine many neurons into layers.")
print("Input layer -> Hidden layers -> Output layer")
