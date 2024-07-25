def idade_filho_mais_velho(M, A, B):
    # Calcula a idade do terceiro filho
    C = M - (A + B)
    
    # Encontra a maior idade entre os três filhos
    return max(A, B, C)

# Leitura dos valores de entrada
M = int(input().strip())
A = int(input().strip())
B = int(input().strip())

# Chamada da função e impressão do resultado
print(idade_filho_mais_velho(M, A, B))