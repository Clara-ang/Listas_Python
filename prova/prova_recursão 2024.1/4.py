def f_rec(a,b):
    if a > b:
        return 0
    else:
        return 1 + f_rec(a + 2, b)
    
x, y = map(int, input().split())
z = f_rec(x, y)
print(z)