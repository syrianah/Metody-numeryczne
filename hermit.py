import math

class Hermit:
    def __init__(self, x_array, y_array, der_array):
        if len(x_array) == len(y_array):
            self.x_array = x_array
            self.y_array = y_array
            self.der_array = der_array
            self.lists = [[] for _ in range(len(self.x_array)+1)]
            self.pol = []
            self.wynik = 0
        else: exit()

    def first(self):
        n = len(self.x_array)
        for i in range(n):
            x = self.x_array[i]
            y = self.y_array[i]
            self.lists[0].append(x)
            self.lists[1].append(y)

    def loop(self):
        self.first()
        k = 0
        c = 0
        for i in range(len(self.lists)-1):
            # print(i)
            x = self.lists[0]
            val = self.lists[i+1]
            # print(val)
            for j in range(len(val)-1):
                # if i+k+1 < len(x)-1:
                if (x[j+k+1] - x[j+k-c] == 0):
                    for i in range(len(self.der_array)-1):
                        wynik = self.der_array[i] / math.factorial(self.der_array[i+1])
                else:
                    wynik = (val[j+1] - val[j]) / (x[j+k+1] - x[j+k-c])

                # print(val[j+1])
                # print(val[j])
                # print(x[j+k+1])
                # print(x[j+k-c])
                # print(wynik)
                self.lists[i+2].append(wynik)
                # else: continue
            k += 1
            c += 1
        self.polym()
        return self.lists, self.pol

    def polym(self):
        for i in range(len(self.lists)):
            if i == 0:
                continue
            else:
                var = self.lists[i]
                # print(var)
                w = var[0]
                # print(w)
                self.pol.append(w)
        return self.pol

    def calculate(self, x):
        self.loop()
        x_arr = self.lists[0]
        xd = []
        for i in range(len(x_arr)-1):
            # print(x_arr[i])
            if i == 0:
                p = x - x_arr[0]
                xd.append(p)
            else:
                w = xd[i-1] * (x - x_arr[i])
                # print(w)
                xd.append(w)
        # print(xd)
        for i in range(len(self.pol)):
            if i == 0:
                self.wynik = self.wynik + self.pol[0]
            else:
                # print(self.pol[i] * xd[i-1])
                self.wynik = self.wynik + (self.pol[i] * xd[i-1])
            # print(self.wynik)
        return self.lists, self.wynik


    def __repr__(self):
        return "{}{}".format(self.lists, self.wynik)


a = Hermit([0, 1, 2, 4, 6, 8, 10, 13, 14], [2, 3, 5, 9, 12, 13, 15, 17, 19], [3, 1, 1, 1, 1, 1, 2, 2])
# a = Hermit([0, 1, 2, 4, 5], [7, 3, -1, 3, -3], [3, 1, 1, 2])
# a = Lagrange([1, 2, 5, 6], [0, 4, 6, -2])
# a = Lagrange([2, 5/2, 4], [0.5, 2/5, 1/4])
# b = a.loop()
b = a.calculate(3)
print(b)
