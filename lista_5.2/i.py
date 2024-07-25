def tempo_total(A1, A2, A3):
    # Calcular o tempo total se a máquina estiver no andar 1
    tempo_1 = A2 * 1 * 2 + A3 * 2 * 2
    
    # Calcular o tempo total se a máquina estiver no andar 2
    tempo_2 = A1 * 1 * 2 + A3 * 1 * 2
    
    # Calcular o tempo total se a máquina estiver no andar 3
    tempo_3 = A1 * 2 * 2 + A2 * 1 * 2
    
    # Retornar o menor tempo total
    return min(tempo_1, tempo_2, tempo_3)

# Leitura dos valores de entrada
A1 = int(input().strip())
A2 = int(input().strip())
A3 = int(input().strip())

# Calcular e imprimir o menor tempo total
resultado = tempo_total(A1, A2, A3)
print(resultado)
