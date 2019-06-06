import numpy as np

class Jacobi:
    def __init__(self, A, b):
        self.maxiter = 100
        self.delta = 10**-10
        self.epsilon = 1/2*10**-4
        self.A = A
        self.b = b

    def calculate(self):
        x = np.array([0, 0, 0])
        n = len(self.b)
        for k in range(1, self.maxiter):
            y = x
            for i in range(n):
                sum = self.b[i]
                diag = self.A[i][i]
                if abs(diag) < self.delta:
                    print("za małe elementy na przekątnej")
                for j in range(n):
                    if j != i:
                        sum = sum - self.A[i][j] * y[j]
                x[i] = sum / diag
                print(k, x)
                if np.linalg.norm(x - y) < self.epsilon:
                    print(k, x)

Q = np.array([[1, 9, 1],
            [4, 1, -1],
            [1, -3, 12]])

b = np.array([5, 3, 31])

x = Jacobi(Q, b)
x.calculate()
