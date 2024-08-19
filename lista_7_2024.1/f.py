def primo_l(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 
n = int(input())

# Verifica se n é primo e imprime o resultado
if primo_l(n):
    print("Sim")
else:
    print("Nao")