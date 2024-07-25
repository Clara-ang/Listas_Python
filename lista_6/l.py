def lista_troca_menor_primeiro(lista):
    if len(lista) <= 1:
        return 0
    
    menor_valor = min(lista)
    indice_menor = lista.index(menor_valor)    
    if indice_menor == 0:
        return 0
    
    # Realizar a troca
    lista[0], lista[indice_menor] = lista[indice_menor], lista[0]
    
    # Retornar a quantidade de trocas realizadas (sempre 1 neste caso)
    return 1