def indice_do_maior(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        ultimo = lista[-1]
        sublista = lista.copy()
        sublista.pop()
        maior = indice_do_maior(sublista)
        if ultimo > maior:
            return ultimo
        else:
            return maior
    

# Testando a função
l = list(map(int, input().split()))
print(indice_do_maior(l))