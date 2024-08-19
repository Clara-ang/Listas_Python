lista = list(map(int, input().split()))
x = lista[0] + lista[1]
lista.append(x)
lista.append(x + lista[2])
lista[0] = lista[3] + lista[4]
lista[1] = lista[4] + lista[5]
lista[4] = lista[4] - lista[2]
print(*lista)