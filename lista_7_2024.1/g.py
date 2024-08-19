n = int(input())
numeros = list(map(int, input().split()))

media = sum(numeros) / n

abaixo = []
igual_ou_acima = []

for num in numeros:
    if num < media:
        abaixo.append(num)
    else:
        igual_ou_acima.append(num)

print(f"{media:.1f}")
print(len(abaixo), " ".join(map(str, abaixo)))
print(len(igual_ou_acima), " ".join(map(str, igual_ou_acima)))