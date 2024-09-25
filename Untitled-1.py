from collections import Counter

def recomendar_cuidados(temperatura, tipo_solo, umidade_solo, exposicao_solar, umidade_ar, estacao):
    """
    Função que recomenda cuidados com plantas com base nas condições ambientais fornecidas.

    Parâmetros:
    - temperatura (float): Temperatura ambiente em graus Celsius.
    - tipo_solo (str): Tipo de solo da planta (arenoso, argiloso, siltoso, humoso, rochoso).
    - umidade_solo (str): Nível de umidade do solo (seco ou úmido).
    - exposicao_solar (float): Quantidade de exposição solar em horas.
    - umidade_ar (float): Umidade do ar em porcentagem.
    - estacao (str): Estação do ano (inverno, primavera, verão, outono).

    Retorna:
    - recomendacoes (list): Lista de recomendações para os cuidados com a planta.
    - decisao_regar (list): Lista de decisões sobre a necessidade de regar a planta.

    A função analisa as condições ambientais e usa um conjunto de regras predefinidas para gerar
    recomendações específicas de cuidados e decisões sobre rega.
    """
    
    recomendacoes = []  # Lista de recomendações a serem fornecidas
    decisao_regar = []  # Decisões sobre rega

    # Regras de cuidados baseadas em cada fator ambiental
    regras_cuidados = {
        "temperatura": {
            "baixo": (15, "evitar", [
                "Traga a planta para dentro de casa para protegê-la do frio.",
                "Considere usar um aquecedor próximo, mas não diretamente."
            ]),
            "alto": (30, "aumentar", [
                "Coloque a planta em um local mais fresco.",
                "Verifique se a planta está recebendo água suficiente para evitar estresse."
            ])
        },
        "umidade_solo": {
            "seco": ("regar levemente", [
                "Verifique se a planta precisa de nutrientes.",
                "Use um fertilizante balanceado para promover um crescimento saudável."
            ]),
            "umido": ("evitar", [
                "Verifique a drenagem do vaso e a saúde das raízes.",
                "Evite regar até que o solo esteja seco ao toque."
            ])
        },
        "exposicao_solar": {
            "alta": (6, [
                "Mover para uma área com sombra parcial para evitar queimar as folhas.",
                "Aplique uma camada de mulch para manter a umidade do solo."
            ]),
            "baixa": (4, [
                "Mover a planta para um local com mais exposição à luz.",
                "Considere o uso de lâmpadas de crescimento se a luz natural for insuficiente."
            ])
        },
        "tipo_solo": {
            "arenoso": ("aumentar", [
                "Adicione matéria orgânica para melhorar a retenção de água.",
                "Certifique-se de que a planta esteja recebendo água suficiente."
            ]),
            "argiloso": ("evitar", [
                "Evite regar em excesso e verifique a compactação do solo.",
                "Considere misturar areia para melhorar a drenagem."
            ]),
            "siltoso": ("regar moderadamente", [
                "Mantenha uma camada de cobertura para evitar erosão.",
                "Verifique regularmente a umidade do solo."
            ]),
            "humoso": ("evitar regas excessivas", [
                "Verifique se a planta está recebendo luz suficiente.",
                "Aplique fertilizantes orgânicos conforme necessário."
            ]),
            "rochosos": ("aumentar", [
                "Certifique-se de que a planta tem espaço suficiente para as raízes.",
                "Verifique a necessidade de nutrientes adicionais."
            ])
        },
        "umidade_ar": {
            "baixo": (40, "regar levemente", [
                "Considere o uso de um umidificador para aumentar a umidade.",
                "Borrife água nas folhas para ajudar a aumentar a umidade."
            ]),
            "alto": (70, "evitar", [
                "Verifique se a ventilação é adequada para evitar mofo.",
                "Certifique-se de que a planta não esteja em uma área estagnada."
            ])
        },
        "estacao": {
            "inverno": (None, [
                "Reduzir o uso de fertilizantes devido ao inverno.",
                "Mantenha a planta em um local mais quente.",
                "Reduza a rega, pois as plantas geralmente necessitam de menos água nesta estação."
            ]),
            "primavera": (None, [
                "Aumentar o uso de fertilizantes devido à fase de crescimento.",
                "Recomende a fertilização a cada duas semanas."
            ]),
            "verao": (None, [
                "Aumentar o uso de fertilizantes devido à fase de crescimento.",
                "Recomende a fertilização a cada duas semanas."
            ]),
            "outono": (None, [
                "Começar a reduzir o uso de fertilizantes.",
                "Prepare a planta para o inverno, reduzindo a rega gradualmente."
            ])
        }
    }

    # Avaliação de temperatura
    if temperatura < regras_cuidados["temperatura"]["baixo"][0]:
        decisao_regar.append(regras_cuidados["temperatura"]["baixo"][1])
        recomendacoes.extend(regras_cuidados["temperatura"]["baixo"][2])
    elif temperatura > regras_cuidados["temperatura"]["alto"][0]:
        decisao_regar.append(regras_cuidados["temperatura"]["alto"][1])
        recomendacoes.extend(regras_cuidados["temperatura"]["alto"][2])

    # Avaliação de umidade do solo
    decisao_regar.append(regras_cuidados["umidade_solo"][umidade_solo][0])
    recomendacoes.extend(regras_cuidados["umidade_solo"][umidade_solo][1])

    # Avaliação de exposição solar
    if exposicao_solar > regras_cuidados["exposicao_solar"]["alta"][0]:
        recomendacoes.extend(regras_cuidados["exposicao_solar"]["alta"][1])
    elif exposicao_solar < regras_cuidados["exposicao_solar"]["baixa"][0]:
        recomendacoes.extend(regras_cuidados["exposicao_solar"]["baixa"][1])

    # Avaliação do tipo de solo
    decisao_regar.append(regras_cuidados["tipo_solo"][tipo_solo][0])
    recomendacoes.extend(regras_cuidados["tipo_solo"][tipo_solo][1])

    # Avaliação de umidade do ar
    if umidade_ar < regras_cuidados["umidade_ar"]["baixo"][0]:
        decisao_regar.append(regras_cuidados["umidade_ar"]["baixo"][1])
        recomendacoes.extend(regras_cuidados["umidade_ar"]["baixo"][2])
    elif umidade_ar > regras_cuidados["umidade_ar"]["alto"][0]:
        decisao_regar.append(regras_cuidados["umidade_ar"]["alto"][1])
        recomendacoes.extend(regras_cuidados["umidade_ar"]["alto"][2])

    # Avaliação da estação do ano
    for chave, valor in regras_cuidados["estacao"].items():
        if chave == estacao:
            recomendacoes.extend(valor[1])
            if chave in ["primavera", "verao"]:
                recomendacoes.append("Recomendar a poda de folhas ou galhos secos para estimular o crescimento de novos brotos.")

    # Remover duplicatas nas recomendações
    recomendacoes = list(set(recomendacoes))

    return recomendacoes, decisao_regar

def decidir_rega(decisoes):
    """
    Função que decide se a planta deve ser regada com base nas decisões de rega acumuladas.

    Parâmetros:
    - decisoes (list): Lista de decisões de rega (aumentar, evitar, regar levemente, etc.).

    Retorna:
    - str: A decisão final sobre a rega da planta com base em uma média ponderada das decisões.
    """
    if not decisoes:
        return "Decisão sobre rega não determinada."

    contagem = Counter(decisoes)
    total_decisoes = sum(contagem.values())

    # Atribuição de pesos para calcular a decisão final
    pesos = {
        "evitar": -1,
        "aumentar": 1,
        "regar levemente": 0.5,
        "regar moderadamente": 0.5,
        "evitar regas excessivas": -0.5
    }

    # Cálculo da média ponderada para determinar a recomendação
    pontuacao_final = sum(pesos[decisao] * contagem[decisao] for decisao in contagem) / total_decisoes

    if pontuacao_final > 0.5:
        return "É recomendado aumentar a frequência da rega."
    elif pontuacao_final < -0.5:
        return "É recomendado evitar regar a planta neste momento."
    else:
        return "Recomenda-se regar levemente a planta."

def processar_dados():
    """
    Função que coleta os dados de entrada do usuário, processa as recomendações e as exibe.
    Solicita temperatura, tipo de solo, umidade do solo, exposição solar, umidade do ar e estação do ano,
    e, com base nesses dados, gera recomendações de cuidados e uma decisão sobre rega.
    """
    try:
        # Coleta de dados do usuário
        temperatura = float(input("Temperatura (°C): "))
        tipo_solo = input("Tipo de Solo (arenoso, argiloso, siltoso, humoso, rochosos): ").lower()
        umidade_solo = input("Umidade do Solo (seco, umido): ").lower()
        exposicao_solar = float(input("Exposição Solar (horas): "))
        umidade_ar = float(input("Umidade do Ar (%): "))
        estacao = input("Estação do Ano (inverno, primavera, verao, outono): ").lower()

        # Gera as recomendações e a decisão sobre rega
        recomendacoes, decisoes_regar = recomendar_cuidados(temperatura, tipo_solo, umidade_solo, exposicao_solar, umidade_ar, estacao)
        decisao_final = decidir_rega(decisoes_regar)
        recomendacoes.append(decisao_final)

        # Exibe as recomendações
        print("\nRecomendações de Cuidados:")
        for recomendacao in recomendacoes:
            print("- " + recomendacao)
    except ValueError:
        print("Erro: Por favor, insira valores válidos.")

# Executa o processamento de dados ao executar o código
processar_dados()
