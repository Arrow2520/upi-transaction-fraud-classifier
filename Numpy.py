import numpy as np
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
c = np.zeros((2, 3, 3, 2))

output = np.ones((5, 5), 'int16')
z = np.zeros((3, 3), 'int16')
z[1, 1] = 9
output[1:4, 1:4] = z
print(output)
array  = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 5, 16]])

