#def multiplos(a, b, m=0, resultado=[]):
    # Caso base: se o próximo múltiplo for maior que b, retornar a lista de resultados
    #if m > b:
        #return resultado
    # Adiciona o múltiplo atual à lista de resultados
    #resultado.append(m)
    # Chamada recursiva para calcular o próximo múltiplo
    #return multiplos(a, b, m + a, resultado)

# Leitura dos dois números inteiros
#a, b = map(int, input().split())

# Inicializa a função recursiva começando pelo primeiro múltiplo de 'a'
#resultado = multiplos(a, b, a)

# Imprime os múltiplos separados por espaço
#print(" ".join(map(str, resultado)))


a, b = map(int, input().split())
multiplos = []

for i in range(1, b // a + 1):
    multiplo = a * i
    if multiplo <= b:
        multiplos.append(multiplo)

print(" ".join(map(str, multiplos)))
