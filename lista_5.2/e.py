def calcula_conta_agua(consumo):
    # Custo inicial com a assinatura básica
    custo = 7
    
    # Consumo adicional acima da franquia de 10m³
    if consumo > 10:
        consumo_adicional = consumo - 10
        
        # Consumo de 11 a 30m³
        if consumo_adicional <= 20:
            custo += consumo_adicional * 1
        else:
            custo += 20 * 1
            consumo_adicional -= 20
            
            # Consumo de 31 a 100m³
            if consumo_adicional <= 70:
                custo += consumo_adicional * 2
            else:
                custo += 70 * 2
                consumo_adicional -= 70
                
                # Consumo acima de 100m³
                custo += consumo_adicional * 5
    
    return custo

# Leitura do valor de entrada
consumo = int(input().strip())

# Cálculo do valor da conta
valor_conta = calcula_conta_agua(consumo)

# Impressão do resultado
print(valor_conta)
