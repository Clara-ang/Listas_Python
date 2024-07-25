def primo_r(n, d):
    if n == d and d == 1:
        return 1 + primo_r(n, d - 1)
    else:
        return primo_r(n, d - 1)
    
def primo(n):
    return primo_r(n, d)

n = int(input())
print(primo(n))