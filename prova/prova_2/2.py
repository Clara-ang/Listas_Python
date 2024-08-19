def f2(x):
    return  x * 3

def g2(a, b):
    ans = a
    while  a < b:
        a = f2(a)
        ans = ans + 1
    return ans

x, y= map(int, input().split())
print(g2(y, x))

