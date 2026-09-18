import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(np.dot(v1, v2))     # 1*4 + 2*5 + 3*6 = 32 (dot product)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)               # matrix multiplication (@ is the operator for it)