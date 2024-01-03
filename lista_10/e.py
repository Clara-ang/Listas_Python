def sequencia_alegre(n, seq):
    diferenca_esperada = set(range(1, n))

    for i in range(n - 1):
        diferenca = abs(seq[i] - seq[i + 1])
        if diferenca not in diferenca_esperada:
            return 'Nao alegre'

    return 'Alegre'

# Processamento de entrada
while True:
    try:
        entrada = input().split()
        n = int(entrada[0])
        seq = list(map(int, entrada[1:]))
        
        # Verificar se a sequência é alegre
        resultado = sequencia_alegre(n, seq)
        
        # Imprimir o resultado
        print(resultado)

    except EOFError:
        break

    

       
