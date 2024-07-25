#  A primeira linha da entrada contém dois inteiros L e D (1 ≤ L, D ≤ 104),
# indicando o comprimento da estrada e a distância entre pedágios, respectivamente.
# A segunda linha contém dois inteiros K e P (1 ≤ K, P ≤ 104 ), indicando o custo por 
# quilômetro percorrido e o valor de cada pedágio. O primeiro pedágio está localizado 
# no quilômetro D da estrada (ou seja, a distância do início da estrada para o primeiro 
# pedágio é D quilômetros).


c = int(input())
d = int(input())
t = int(input())
d_restante = d - t * c
c_minimo = d_restante / c
print(c_minimo)
 
 