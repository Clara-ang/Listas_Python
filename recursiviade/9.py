def soma_pares(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[-1] + soma_pares(lista[:-1])
    
    
lista = list(map(int, input().split()))
soma = soma_pares(lista)