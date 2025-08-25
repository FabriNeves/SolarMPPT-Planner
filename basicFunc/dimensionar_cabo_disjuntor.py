# Dicionário dos métodos
metodosB1 = {
    "Metodo": "B1 (EPR/XLPE)",
    "Secao_nominal_mm2": [
        0.5, 0.75, 1, 1.5, 2.5, 4, 6, 10, 16, 25,
        35, 50, 70, 95, 120, 150, 185, 240, 300,
        400, 500, 630, 800, 1000
    ],
    "2_condutores_carregados": [
        9, 11, 14, 17.5, 24, 32, 41, 57, 76, 101,
        125, 151, 192, 232, 269, 309, 353, 415, 477,
        571, 656, 758, 881, 1012
    ],
    "3_condutores_carregados": [
        8, 10, 12, 15.5, 21, 28, 36, 50, 68, 89,
        110, 134, 171, 207, 239, 275, 314, 370, 426,
        510, 587, 678, 788, 906
    ]
}

# Disjuntores comerciais
djComerciais = [10,16,20,25,32,40,50,63,70,80,100,125,150,175,200,225]

# Função auxiliar: retorna o menor valor da lista >= procurado
def buscaValorMaior(valorProcurado, lista):
    for i, val in enumerate(lista):
        if val >= valorProcurado:
            return val, i
    # se não encontrar, devolve o último
    return lista[-1], len(lista) - 1

# Função principal
def dimensionar_cabo_disjuntor(corrente_projeto, n_condutores):
    if n_condutores not in [2, 3]:
        raise ValueError("Número de condutores deve ser 2 ou 3")

    # Escolhe a tabela de capacidade conforme os condutores
    chave = f"{n_condutores}_condutores_carregados"
    capacidade = metodosB1[chave]

    # Busca seção mínima que atende
    corrente_cabo, indice = buscaValorMaior(corrente_projeto, capacidade)
    secao = metodosB1["Secao_nominal_mm2"][indice]

    # Busca disjuntor adequado
    disjuntor, _ = buscaValorMaior(corrente_projeto, djComerciais)

    return {
        "CorrenteProjeto": corrente_projeto,
        "CondutoresCarregados": n_condutores,
        "SecaoCabo_mm2": secao,
        "Disjuntor_A": disjuntor
    }
