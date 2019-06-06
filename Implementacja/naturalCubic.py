import numpy as np

class NaturalCubicSpline(object):
    def __init__(self, x, y):
        if len(x) == len(y):
            self.x = x
            self.y = y
            self.z = [0] * (len(self.x)+1)
            self.h = []
            self.b = []
            self.u = []
            self.v = []
        else: exit()

    def interpolate(self):
        # print(self.z[len(self.x)-1])
        for i in range(0, len(self.x)-1):
            self.h.insert(i, self.x[i+1] - self.x[i])
            self.b.insert(i, (self.y[i+1] - self.y[i]) / self.h[i])
        self.u.insert(0, 2 * (self.h[0] + self.h[1]))
        # print(self.u[0])
        self.v.insert(0, 6 * (self.b[1] - self.b[0]))
        # print(self.u[0])
        for i in range(1, len(self.x)-1):
            # print(i)
            self.u.insert(i, 2 * (self.h[i] + self.h[i-1]) - self.h[i-1]**2 / self.u[i-1])
            self.v.insert(i, 6 * (self.b[i] - self.b[i-1]) - self.h[i-1] * self.v[i-1] / self.u[i-1])
        # print(self.z[len(self.x)])
        print(self.u, self.v)
        for i in range(len(self.x)-2, 1, -1):
            # print(i)
            self.z.insert(i, (self.v[i] - self.h[i] * self.z[i+1]) / self.u[i])
        return self.h, self.b, self.u, self.v

    def SplineEval(self, x):
        self.interpolate()
        for i in range(len(self.x)-2, 0, -1):
            if x - self.x[i] >= 0:
                break
        h = self.x[i+1] - self.x[i]
        tmp = (self.z[i]/2) + (x - self.x[i]) * (self.z[i+1] - self.z[i]) / 6 * h
        tmp = -(h / 6) * (self.z[i+1] + 2 * self.z[i]) + (self.y[i+1] - self.y[i]) / h + (x - self.x[i]) * tmp
        return self.y[i] + (x - self.x[i]) * tmp

X = []
Y = []
xd = 0

for x in np.arange(-1, 1, 0.0952381):
    X.append(x)
    xd = xd + 1
    y = 1/(1 + 6*x**2)
    Y.append(y)

print(xd)
print(X)
print(Y)
a = NaturalCubicSpline([1, 2, 5, 6], [0, 4, 6, -2])
a = NaturalCubicSpline(X, Y)
# print(a.interpolate())
print(a.SplineEval(3))
