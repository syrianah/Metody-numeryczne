import numpy as np

class Richardson:
    def __init__(self, A, b):
        self.maxiter = 10
        self.delta = 10**-10
        self.epsilon = 1/2*10**-4
        self.A = A
        self.b = b

    def calculate(self):
        x = np.array([0, 0, 0])
        n = len(x)
        Q = np.identity(n)
        for k in range(self.maxiter):
            y = x
            c = (Q - self.A) * x + self.b
            x = c * np.linalg.inv(Q)
            print(k, x)
            if np.linalg.norm(x - y) < self.epsilon:
                print("convergence")

Q = np.array([[1, 9, 1],
            [4, 1, -1],
            [1, -3, 12]])

b = np.array([5, 3, 31])

x = Richardson(Q, b)
x.calculate()
