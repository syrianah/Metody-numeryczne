import numpy as np

class Solution:
    def __init__(self, A, b):
        self.maxiter = 100
        self.delta = 10**-10
        self.epsilon = 1/2*10**-4
        self.omega = 2
        self.A = A
        self.b = b
        self.x = np.zeros(len(b))
        self.n = len(self.x)

    def gauss(self):
        for k in range(1, self.maxiter):
            y = self.x
            for i in range(self.n):
                sum = self.b[i]
                diag = self.A[i][i]
                if abs(diag) < self.delta:
                    print("za małe elementy na przekątnej")
                for j in range(i-1):
                    sum = sum - np.multiply(self.A[i][j], self.x[i])
                for j in range(i+1, self.n):
                    sum = sum - np.multiply(self.A[i][j], self.x[i])
                self.x[i] = sum / diag
                print(k, self.x)
                if np.linalg.norm(self.x - y) < self.epsilon:
                    print(k, self.x)

    def sor(self):
        for k in range(1, self.maxiter):
            y = self.x
            for i in range(self.n):
                sum = self.b[i]
                diag = self.A[i][i]
                if abs(diag) < self.delta:
                    print("za małe elementy na przekątnej")
                for j in range(i-1):
                    sum = sum - np.multiply(self.A[i][j], self.x[i])
                for j in range(i+1, self.n):
                    sum = sum - np.multiply(self.A[i][j], self.x[i])
                self.x[i] = sum / diag
                self.x[i] = self.omega * self.x[i] + (1 - self.omega) * y[i]
                print(k, self.x)
                if np.linalg.norm(self.x - y) < self.epsilon:
                    print(k, self.x)

    def jacobi(self):
        for k in range(1, self.maxiter):
            y = self.x
            for i in range(self.n):
                sum = self.b[i]
                diag = self.A[i][i]
                if abs(diag) < self.delta:
                    print("za małe elementy na przekątnej")
                for j in range(self.n):
                    if j != i:
                        sum = sum - np.multiply(self.A[i][j], y[i])
                self.x[i] = sum / diag
                print(k, x)
                if np.linalg.norm(self.x - y) < self.epsilon:
                    print(k, self.x)

    def richardson(self):
        Q = np.identity(self.n)
        for k in range(self.maxiter):
            y = self.x
            c = (Q - self.A) * self.x + self.b
            self.x = c * np.linalg.inv(Q)
            print(k, self.x)
            if np.linalg.norm(self.x - y) < self.epsilon:
                print("convergence")


#Współczynniki:
Q = np.array([[1, 9, 1],
            [4, 1, -1],
            [1, -3, 12]])

#Wartości:
b = np.array([5, 3, 31])

x = Solution(Q, b)

#Wywołania metod:
# x.richardson()
# x.jacobi()
# x.gauss()
x.sor()
