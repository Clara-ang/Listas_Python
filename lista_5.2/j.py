def pode_preservar_projeto(a1, a2, a3, a4):
    areas = [a1, a2, a3, a4]
    areas.sort()  # Ordenar as áreas para facilitar a comparação
    
    # Somar as áreas
    total_area = sum(areas)
    
    # Verificar todas as combinações possíveis
    # Verificar se duas somas de pares iguais a total_area/2
    if (areas[0] + areas[3] == areas[1] + areas[2]):
        return 'S'
    return 'N'

# Leitura dos valores de entrada
A1, A2, A3, A4 = map(int, input().strip().split())

# Calcular e imprimir o resultado
resultado = pode_preservar_projeto(A1, A2, A3, A4)
print(resultado)
