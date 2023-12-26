# Encontrando e mostrando números de lista02 que não estão em lista01
def f(l01, l02):
    n = 0
    for i in range(len(l01)):
        for j in range(len(l02)):
            if l01[i] not in l02[j] :
                n= n + 1
                break
    return n
listal = list(map(int, input().split())) 
lista2 = list(map(int, input().split())) 
print(f(listal, lista2))

