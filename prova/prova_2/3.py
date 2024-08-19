def f3(x):
    if x == 0:
        return 0
    q = 0
    if x % 2 == 1:
        q = 1
    return q + f3(x // 2)

x = int(input())
print(f3(x))

