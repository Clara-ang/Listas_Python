n = int(input())
numeros = list(map(int, input().split()))

media = sum(numeros) / n

abaixo = 0
igual_ou_acima = 0

for num in numeros:
    if num < media:
        abaixo += 1
    else:
        igual_ou_acima += 1

print(f"{media:.1f}")
print(abaixo)
print(igual_ou_acima)
