# ==============================
# DICIONÁRIO DOS MÉTODOS (B1)
# ==============================
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

# ==============================
# DISJUNTORES COMERCIAIS
# ==============================
djComerciais = [
    10, 16, 20, 25, 32, 40, 50, 63, 70, 80,
    100, 125, 150, 175, 200, 225
]


# ==============================
# FUNÇÕES AUXILIARES
# ==============================

def buscaValorMaior(valorProcurado, lista):
    """
    Retorna o menor valor da lista que seja >= procurado.
    Caso não encontre, retorna o último valor.
    """
    for i, val in enumerate(lista):
        if val >= valorProcurado:
            return val, i
    return lista[-1], len(lista) - 1


def calcular_queda_tensao(L, Ib, Vff, modo=2, secao_mm2=None, deltaV_percent=None, p=1.72e-8):
    """
    Calcula a queda de tensão percentual (%ΔV) ou a seção necessária do condutor.

    Fórmulas:
    - Bifásico (modo=2): ΔV = (2 * p * L * Ib) / S
    - Trifásico (modo=3): ΔV = (√3 * p * L * Ib) / S

    Parâmetros:
    - L: comprimento total do circuito (m)
    - Ib: corrente (A)
    - Vff: tensão entre fases (V)
    - modo: 2 = bifásico, 3 = trifásico
    - secao_mm2: seção do condutor (mm²), calcula %ΔV
    - deltaV_percent: queda desejada (%), calcula seção
    - p: resistividade do material (Ω·m), cobre = 1.72e-8

    Retorno:
    - % queda de tensão ou seção necessária (mm²)
    """
    if modo == 2:
        fator = 2
    elif modo == 3:
        fator = 1.732
    else:
        raise ValueError("Modo inválido. Use 2 para bifásico ou 3 para trifásico.")

    if secao_mm2 is not None:
        secao_m2 = secao_mm2 * 1e-6
        deltaV = (fator * p * L * Ib) / secao_m2
        return round((deltaV / Vff) * 100, 2)

    elif deltaV_percent is not None:
        secao_m2 = (fator * p * L * Ib) / ((deltaV_percent / 100) * Vff)
        return round(secao_m2 * 1e6, 2)

    else:
        raise ValueError("Informe 'secao_mm2' ou 'deltaV_percent'.")


# ==============================
# FUNÇÕES DE DIMENSIONAMENTO
# ==============================

def dimensionar_cabo_disjuntor(corrente_projeto, n_condutores):
    """
    Dimensiona cabo e disjuntor para a corrente de projeto.
    """
    if n_condutores not in [2, 3]:
        raise ValueError("Número de condutores deve ser 2 ou 3.")

    chave = f"{n_condutores}_condutores_carregados"
    capacidade = metodosB1[chave]

    # Escolhe seção mínima que atenda a corrente
    corrente_cabo, indice = buscaValorMaior(corrente_projeto, capacidade)
    secao = metodosB1["Secao_nominal_mm2"][indice]

    # Escolhe disjuntor adequado
    disjuntor, _ = buscaValorMaior(corrente_projeto, djComerciais)

    return {
        "CorrenteProjeto": corrente_projeto,
        "CondutoresCarregados": n_condutores,
        "SecaoCabo_mm2": secao,
        "Disjuntor_A": disjuntor
    }


def dimensionar_cabo_disjuntor_ajustado(tensao_linha, corrente_projeto, n_condutores, comprimento, limite_queda=1):
    """
    Dimensiona cabo e disjuntor considerando queda de tensão.
    Ajusta a seção até que a queda seja <= limite (%).
    """
    resultado = dimensionar_cabo_disjuntor(corrente_projeto, n_condutores)
    secao_atual = resultado["SecaoCabo_mm2"]

    # Calcula queda de tensão inicial
    quedaTensao = calcular_queda_tensao(comprimento, corrente_projeto, tensao_linha, n_condutores, secao_atual)
    index = metodosB1["Secao_nominal_mm2"].index(secao_atual)
    tamLista = len(metodosB1["Secao_nominal_mm2"])

    # Ajusta até atender o limite
    while quedaTensao > limite_queda and index < tamLista - 1:
        index += 1
        secao_atual = metodosB1["Secao_nominal_mm2"][index]
        quedaTensao = calcular_queda_tensao(comprimento, corrente_projeto, tensao_linha, n_condutores, secao_atual)

    return {
        "CorrenteProjeto": corrente_projeto,
        "CondutoresCarregados": n_condutores,
        "SecaoCabo_mm2": secao_atual,
        "Disjuntor_A": resultado["Disjuntor_A"],
        "QuedaTensao_percent": quedaTensao
    }


# ==============================
# EXEMPLOS DE USO
# ==============================

print(dimensionar_cabo_disjuntor(40, 2))
print(dimensionar_cabo_disjuntor_ajustado(220, 40, 2, 15))
