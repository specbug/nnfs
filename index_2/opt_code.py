# 3x2 NN (populated random values)
import numpy as np

inputs = [1.2, 5.1, 2.0] # (m1, m2, m3)
weights = [[0.2, 1.2, 1.6],
		   [3.7, 1.0, 0.6]] # weights for all neurons (n1 & n2)
biases = [1.2, 0.3] # biases for all neurons (n1 & n2)

outputs = np.dot(weights, inputs) + biases

print(outputs) # calculated values for layer 2 (n1 & n2)
# [10.76, 11.04]