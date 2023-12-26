def g(l01):
    if len(l01) == 0: 
        return 10000 
    else:
        n = l01[- 1] 
        if n % 2==0 and n > 0: 
            return min(n, g (l01[:-1]))
        else: 
            return g (l01[:-1])
        
lista = list(map(int, input().split()))
print(g(lista))