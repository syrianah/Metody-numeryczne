def first(x_array, y_array, lists):
    if len(x_array) == len(y_array):
        n = len(x_array)
    else: exit()
    i = 0
    while i < n:
        if i < n-1:
            wynik = (y_array[i+1] - y_array[i]) / (x_array[i+1] - x_array[i])
            lists[0].append(wynik)
            i += 1
        else: break

def last(x_array, lists):
    list = lists[0]
    i = 0;
    while i < len(x_array)-1:
        if i < len(list)-1:
            wynik = (list[i+1] - list[i]) / (x_array[len(x_array)-1] - x_array[0])
            lists[len(lists)-1].append(wynik)
            i += 1
        else: break

def lagrange(x_array, y_array):
    lists = [[] for _ in range(len(x_array)-1)]
    first(x_array, y_array, lists)
    if len(lists) > 2:
        pass
        if len(lists) > 3:
            pass
    else:
        last(x_array, lists)
    return lists

print(lagrange([2, 5/2, 4], [0.5, 2/5, 1/4]))
