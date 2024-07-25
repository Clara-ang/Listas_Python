def sublista_sem_menor(lista):
    if not lista:  
        return []
    
    menor = min(lista)
    lista_b = []

    encontrado = False  # Para garantir que removemos apenas uma instância do menor elemento
    for elemento in lista:
        if elemento == menor and not encontrado:
            encontrado = True  # Marcar que já removemos uma instância do menor elemento
        else:
            lista_b.append(elemento)
    

    return lista_b

exemplo_lista = [2, 4, 6, 8, 1, 3, 5, 7]
print(sublista_sem_menor(exemplo_lista))

def sublista_sem_menor(lista):
    if not lista:
        return lista  # Se a lista estiver vazia, retorna a lista vazia
    
    menor = min(lista)
    lista_b = lista.copy()  # Faz uma cópia da lista original
    lista_b.remove(menor)  # Remove a primeira ocorrência do menor elemento
    
    return lista_b
