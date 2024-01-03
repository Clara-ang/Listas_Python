def vender_chinelos(N, estoque, P, pedidos):
    vendas = 0

    for pedido in pedidos:
        tamanho_chinelo = pedido - 1    # Ajuste para índice 0-based

        # Verifica se o tamanho do chinelo é válido e há estoque disponível
        if 0 <= tamanho_chinelo < N:
            if estoque[tamanho_chinelo] >= 0:
                vendas += 1
                estoque[tamanho_chinelo] -= 1

    return vendas

# Leitura de entrada
N = int(input())
estoque = list(map(int, input().split()))  # Agora é uma única lista
P = int(input())
pedidos = [int(input()) for _ in range(P)]

# Cálculo e impressão do resultado
resultado = vender_chinelos(N, estoque, P, pedidos)
print(resultado)
