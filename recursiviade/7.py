def cont_divisores (n, k):
    if k == 1:
        return [1]
    else:
        qtd = cont_divisores(n, k - 1)
        if n % k == 0:
            qtd.append(k)
        return qtd
def divisores(n):
    return cont_divisores(n, n)

    
div = int(input())
q = divisores(div)
print(q)
