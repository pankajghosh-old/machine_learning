import numpy as np

input = np.array([[0,0], [0,1], [1,0], [1,1]])
threshold = 1

and_weights = np.array([0.5,0.5])

and_output = np.dot(input, and_weights) >= threshold
print and_output
print and_output.astype(int)

#xor
xor_layer_1 = np.array([[1,0], [0.5,0.5], [0,1]])
xor_layer_1_output = np.dot(input, np.transpose(xor_layer_1)) >= threshold
print xor_layer_1_output
print xor_layer_1_output.astype(int)

xor_layer_2 = np.array([1,-2,1])
xor_layer_2_output = np.dot(xor_layer_1_output, np.transpose(xor_layer_2)) >= threshold
print xor_layer_2_output
print xor_layer_2_output.astype(int)
