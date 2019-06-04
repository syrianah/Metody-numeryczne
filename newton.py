def f(x):
    return x**3 - x**2 + 3

def fp(x):
    return 3*x**2 - 2*x

def newton(x):
    x_tab = []
    x_tab.append(x)
    for i in range(4):
        temp =  x_tab[i] - f(x_tab[i]) / fp(x_tab[i])
        x_tab.append(temp)
    return x_tab

print(newton(-2))