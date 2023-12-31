def contar_convidados(N, P, pontuacoes):
    convidados = 0
    for i in range(N):
        total_pontos = pontuacoes[i][0] + pontuacoes[i][1]
        if total_pontos >= P:
            convidados += 1
    return convidados


N, P = map(int, input().split())
pontuacoes = [list(map(int, input().split())) for _ in range(N)]


resultado = contar_convidados(N, P, pontuacoes)
print(resultado)
