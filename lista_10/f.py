def colorir_fita(N, fita):
    # Inicialize uma lista para armazenar as distâncias dos quadrados não coloridos para o tom 0
    distancias = [float('inf')] * N

    # Verifique os quadrados à esquerda de cada quadrado colorido
    for i in range(N):
        if fita[i] == 0:
            distancias[i] = 0
            for j in range(i - 1, -1, -1):
                distancias[j] = min(distancias[j], i - j)

    # Verifique os quadrados à direita de cada quadrado colorido
    for i in range(N - 1, -1, -1):
        if fita[i] == 0:
            distancias[i] = 0
            for j in range(i + 1, N):
                distancias[j] = min(distancias[j], j - i)

    for i in range(N):
        if fita[i] == -1:
            fita[i] = min(distancias[i], 9)

    print(*fita)


N = int(input())
fita = list(map(int, input().split()))

colorir_fita(N, fita)