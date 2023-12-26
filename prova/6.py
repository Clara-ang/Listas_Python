lista1 = list(map(int, input().split())) 
lista2 = list(map(int, input().split())) 

n_nao_presentes = [num for num in lista2 if num not in lista1]

print(f"{n_nao_presentes}")
#print(f(listal, lista2))
