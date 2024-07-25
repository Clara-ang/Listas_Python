def dia(dia, mes, ano):
    dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    nomes_meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", 
                   "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    if mes < 1 or mes > 12:
        return "Data Invalida"
    
    if dia < 1 or dia > dias_no_mes[mes - 1]:
        return "Data Invalida"
    
    dia_formatado = f"{dia:02d}"
    
    data_por_extenso = f"{dia_formatado} de {nomes_meses[mes - 1]} de {ano}"
    
    return data_por_extenso


def dia(dia, mes, ano):
    # Verificação básica do intervalo
    if not (1 <= dia <= 31) or not (1 <= mes <= 12):
        return "Data Invalida"
    
    # Mapeamento dos meses para os seus nomes
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", 
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    # Verificação do dia para cada mês
    if mes == 2 and dia > 28:
        return "Data Invalida"
    elif mes in [4, 6, 9, 11] and dia > 30:
        return "Data Invalida"
    elif dia > 31:
        return "Data Invalida"
    
    # Formatar o dia com dois dígitos
    dia_formatado = f"{dia:02d}"
    
    # Obter o nome do mês
    nome_mes = meses[mes - 1] # Qualquer coisa na lista com -1 o se refere ao ultimo elemento da lista.
    
    # Construir a data por extenso
    data_por_extenso = f"{dia_formatado} de {nome_mes} de {ano}"
    
    return data_por_extenso