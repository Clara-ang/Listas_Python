a, b = map(int, input().split())
mult = []

for i in range(a, b + 1, a):
    mult.append(i)

print(" ".join(map(str, mult)))