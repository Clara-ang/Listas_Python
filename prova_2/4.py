def f4_r(n, d):
    if d==0: 
        return [] 
    x=f4_r(n,d-1) 
    if n % d == 0: 
        x.append(d)
    return x
def f4(n,):
    return f4_r(n, n)


x = int(input())

print(f4(x))