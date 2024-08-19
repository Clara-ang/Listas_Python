#import sys
#sys.setrecursionlimit(100000)
#def somatorio(n):
#    if (n == 0):
#        return 0
#    # Caso base: se n for 1, retorna 1.0
#    if n == 1:
#        return 1.0
#    # Chamada recursiva: soma 1/n ao resultado da chamada recursiva para n-1
#    return 1/n + somatorio(n-1)

# Leitura do número inteiro
#n = int(input())

# Calcula o somatório e imprime o resultado com 4 casas decimais
#resultado = somatorio(n)
#print(f"{resultado:.4f}")

def calcular_somatorio(n):
   soma = 0.0
   for i in range(1, n + 1):    
      soma +=  1 / i
   return soma

n = int(input())

resultado = calcular_somatorio(n)
print(f"{resultado:.4f}")

