import numpy as np

Q = np.array([[1, 9, 1],
            [4, 1, -1],
            [1, -3, 12]])

I = np.array([[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]])

L = np.array([[0, 0, 0],
            [4, 0, 0],
            [1, -3, 0]])

D = np.array([[1, 0, 0],
            [0, 1, 0],
            [0, 0, 12]])

U = np.array([[0, 9, 1],
            [0, 0, -1],
            [0, 0, 0]])

x = np.array([[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]])

# x = np.array([[0], [0], [0]])

b = np.array([5, 3, 31])

A = L + D + U

R = A - D

print(A)

# x = np.zeros(3)

# sum = np.dot(A, x)
# print(sum)

for i in range(2):
    x[i+1] = x[i] - np.dot(A, x[i]) + b[i]

print(x)
