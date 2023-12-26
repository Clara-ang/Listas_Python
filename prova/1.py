def func1(l01):
    k = 0
    for i in range(1, len(l01)): 
        if l01[i] < l01[i - 1] : 
            k = k + 1
    return k


lista = list(map(int, input().split()))
lista.append(1)
q = func1(lista)
print(q)