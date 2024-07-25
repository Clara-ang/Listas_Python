def dia_da_semana(h, d):
    dias = {
        "Domingo": 0,
        "Segunda-feira": 1,
        "Terca-feira": 2,
        "Quarta-feira": 3,
        "Quinta-feira": 4,
        "Sexta-feira": 5,
        "Sabado": 6
    }
    dias_invertido = [
        "Domingo", "Segunda-feira", "Terca-feira",
        "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"
    ]
    dia_atual_num = dias[h]
    dia_evento_num = (dia_atual_num + d) % 7

    return dias_invertido[dia_evento_num]


def dia_da_semana(h, d):
    # Lista com os dias da semana em ordem
    dias_semana = ["Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    
    # Encontrar o índice do dia atual
    indice_atual = dias_semana.index(h)
    
    # Calcular o novo índice
    novo_indice = (indice_atual + d) % 7
    
    # Retornar o dia da semana correspondente ao novo índice
    return dias_semana[novo_indice]
