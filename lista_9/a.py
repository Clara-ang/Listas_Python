jogadores, rodadas = map(int,input().split())
p = list(map(int,input().split()))

p_total = [0] * jogadores
for i in range (jogadores):
    for j in range(i * rodadas, (i + 1) * rodadas):
         p_total[i] += p[j]
         if p_total == jogadores:
            vencedor = p_total.index(max(p_total))
         if p_total > jogadores:
             

    print(vencedor)
   