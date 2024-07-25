B = int(input())
T = int(input())

largura_total = 160
altura = 70

area_total = largura_total * altura

area_felix = (B + T) * altura / 2

area_marzia = (largura_total - B + largura_total - T) * altura / 2

meia_area = area_total / 2

if area_felix > meia_area:
    print(1)
elif area_marzia > meia_area:
    print(2)
else:
    print(0)

