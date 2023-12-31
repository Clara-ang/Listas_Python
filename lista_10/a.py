n = int(input())
estoque = list(map(int, input().split()))
p = int(input())
pedidos = int(input())

vendas_totais = 0

for i in range (1, n, len(estoque), p, len(pedidos)):
    tamanho_chinelo = pedidos - 1  # Ajuste para índice 0-based
    if 0 <= tamanho_chinelo[0] < n and estoque[tamanho_chinelo[0]] > 0:
        vendas_totais += 1
        estoque[tamanho_chinelo[0]] -= 1

print(vendas_totais)

