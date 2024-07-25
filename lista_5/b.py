#def pode_formar_triangulo(A, B, C, D):
    #combinacoes = [
        #(A, B, C),
        #(A, B, D),
        #(A, C, D),
        #(B, C, D)
    #]
    
    # for a, b, c in combinacoes:
      # f a + b > c and a + c > b and b + c > a:
     #       return 'S'
    #return 'N'


a, b, c, d = map(int, input().split())
#print(pode_formar_triangulo(A, B, C, D))

#(a, b, c),
#(a, b, d),
#(a, c, d),
#(b, c, d)

if c + b > a and c + a > b and b + a > c:
    print('S')
elif d + b > a and d + a > b and b + a > d:
    print('S')
elif d + c > a and d + a > c and c + a > d:
    print('S')
elif d + c > b and d + b > c and c + b > d:
    print('S')
else:
    print('N')
