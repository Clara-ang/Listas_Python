#Escreva uma função recursiva que receba um número inteiro n e retorne ]
#a quantidade de algarismo hexadecimal para representar n.#
def qtd_hexa(n):
    if n < 16:
        return 1
    else:
        return 1 + qtd_hexa(n // 16)
    
n = int(input())
print(qtd_hexa(n))