def conta_algarismos(n):
    if n < 10:
        return 1
    else:
        return 1 + conta_algarismos(n // 10)

num = int(input())
q = conta_algarismos(num)
print(q)