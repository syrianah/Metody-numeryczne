class Lagrange:
    def __init__(self, x_array, y_array):
        if len(x_array) == len(y_array):
            self.x_array = x_array
            self.y_array = y_array
            self.lists = [[] for _ in range(len(self.x_array)+1)]
            self.pol = []
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
        m = len(self.lists)
        j = 0
        last = self.lists[m-2]
        x = self.lists[0]
        if m > 3:
            i = 0
            j = 0
            while i < m-1:
                if i < m-1:
                    var1 = self.lists[0]
                    var2 = self.lists[i+1]
                else: break
                while j < len(var1)-1:
                    if j < len(var1)-1:
                        wynik = (var2[i+1] - var2[i]) / (var1[j+1] - var1[j])
                        if m-1 > i+2:
                            self.lists[i+2].append(wynik)
                        else: break
                        j += 2
                        # print(j)
                        # print(self.lists)
                    else:
                        j = 0
                        break
                i += 1
                j = 0
            wynik = (last[1] - last[0]) / (x[len(x)-1] - x[0])
            self.lists[len(self.lists)-1].append(wynik)
            self.polym()
            return "{}{}".format(self.lists, self.pol)

    def polym(self):
        for i in range(len(self.lists)):
            if i == 1:
                continue
            else:
                var = self.lists[i]
                print(var)
                w = var[0]
                print(w)
                self.pol.append(w)
        return self.pol

    def __repr__(self):
        return str(self.lists)

a = Lagrange([1, 2, 5, 6], [0, 4, 6, -2])
# a = Lagrange([2, 5/2, 4], [0.5, 2/5, 1/4])
b = a.loop()
print(b)
