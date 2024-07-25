def divisores_impares(num, d = 1):
         if num == d:
                return 0
         
         if num % d == 0 and num % 2 != 1:
             return 1 + divisores_impares(num, d + 1)
         else:
            return divisores_impares(num, d + 1)

divisores = int(input())
q = divisores_impares(divisores)
print(q)