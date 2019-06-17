import math

# def sort(x):
#     for i in range(len(x)/2):
#         prev = x[i+1]

#         if prev >
def MaxS(l):
    max=0
    for i in l:
        if len(i) > max:
            max=len(i)
    return max

def translate(l):
    x_array = []
    y_array = []
    der_array = []
    k = 0
    print(l)
    for i in range(0, len(l)):
        point = l[i][0]
        # print(point)
        value = l[i][1]
        # print(value)
        for k in range(0, len(l[i])-1):
            x_array.append(point)
            y_array.append(value)

    for temp in l:
        del temp[0]
        del temp[0]
    S=0
    Smax=MaxS(l)
    while S<=Smax+1:
        for i in l:
            if not i:
                continue
            else:
                iN = len(i)
                #print(translate([[0, 7, 3, 1, 4], [1, 3], [2, -1], [4, 3, 1], [5, -3, 1, 2]]))
                print(iN," ",S," ",i," ",der_array)
                if iN==1:
                    der_array.append(i[0])
                    der_array.append(S+1)
                    del i[0]
                else:
                    for j in range (iN):
                        try:
                            der_array.append(i[0])
                            der_array.append(S+1)
                        except:
                            pass
                    try:
                        del i[0]
                    except:
                        pass

        S += 1

    # return x_array, y_array, der_array
    return Hermit(x_array, y_array, der_array)



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
        z = 0
        for i in range(len(self.lists)-1):
            # print(i)
            x = self.lists[0]
            val = self.lists[i+1]
            # print(val)
            for j in range(len(val)-1):
                # print(j)
                # if i+k+1 > len(val)-1:
                #     break               
                if (x[j+k+1] - x[j+k-c] == 0 and val[j+1] - val[j] == 0):
                    wynik = self.der_array[z] / math.factorial(self.der_array[z+1])
                    z = z + 2
                    # print(wynik)
                else:
                    wynik = (val[j+1] - val[j]) / (x[j+k+1] - x[j+k-c])
                    # print(wynik)

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
                self.pol
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


# a = Hermit([0, 0, 1, 2, 4, 4, 5, 5, 5], [7, 7, 3, -1, 3, 3, -3, -3, -3], [3, 1, 1, 1, 1, 1, 1, 1, 2, 2])
# a = Hermit([0, 1, 2, 4, 5], [7, 3, -1, 3, -3], [3, 1, 1, 2])
# a = Lagrange([1, 2, 5, 6], [0, 4, 6, -2])
# a = Lagrange([2, 5/2, 4], [0.5, 2/5, 1/4])
# b = a.loop()
# b = a.calculate(3)
# print(b)
# print(translate([[0, 7, 3], [1, 3], [2, -1], [4, 3, 1], [5, -3, 1, 2]]))

# a = translate([[0, 7, 3], [1, 3], [2, -1], [4, 3, 1], [5, -3, 1, 2]])
# a = translate([[-1, 2, -8, 56], [0, 1, 0, 0], [1, 2, 8, 56]])
# print(translate([[-1, 2, -8, 56], [0, 1, 0, 0], [1, 2, 8, 56]]))
# a = Hermit([-1, -1, -1, 0, 0, 0, 1, 1, 1], [2, 2, 2, 1, 1, 1, 2, 2, 2], [-8, 1, -8, 1, 0, 1, 0, 1, 8, 1, 8, 1, 56, 2, 0, 2, 56, 2])
# b = a.calculate(3)
# print(b)

#Dane od prowadzącego
# a = translate([[0, 3, -7, 12], [1, 2, 11, 62]]) 
# a = Hermit([0,0,0,1,1,1],[3,3,3,2,2,2],[-7,1,-7,1,11,1,11,1,12,2,62,2])
# print(a)
# b = a.calculate(3) 
# print(b)

# Przykład b
# a = translate([[0, 0, 1], [1,3,6]])
# a = Hermit([0,0,1,1],[0,0,3,3],[1,1,6,1])
# print(a.calculate(3))

#Przykład c
a = translate([[1,0,3],[2,6,7,8]])
# a = Hermit([1,1,2,2,2],[0,0,6,6,6],[3,1,7,1,7,1,8,2])
print(a.calculate(3))
# print(a)

# Przykład d
# a = translate([[1,0,3],[2,0,2,2]])
# a = Hermit([1,1,2,2,2],[0,0,0,0,0],[3,1,2,1,2,1,2,2])
# print(a.calculate(3))

# Zadanie 4.7
# a = translate([[0,1,1,1,1,1]])
# print(a.calculate(3))
