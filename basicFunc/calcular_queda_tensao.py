def calcular_queda_tensao(L, Ib, Vff, modo=2, secao_mm2=None, deltaV_percent=None, p=1.72e-8):
    """
    Calcula a queda de tensão percentual (%ΔV) ou a seção necessária do condutor
    para circuitos bifásicos (modo=2) ou trifásicos (modo=3).

    Fórmulas:
    - Bifásico: Sc = (2 * p * L * Ib) / (%ΔV * Vff)
    - Trifásico: Sc = (173.2 * p * L * Ib) / (%ΔV * Vff)

    Parâmetros:
    - L: comprimento total (ida e volta) em metros
    - Ib: corrente (A)
    - Vff: tensão entre fases (V)
    - modo: 2 = bifásico, 3 = trifásico
    - secao_mm2: seção do condutor (mm²), calcula %ΔV se fornecido
    - deltaV_percent: % queda desejada, calcula seção se fornecido
    - p: resistividade (Ω·m), padrão do cobre: 1.72e-8

    Retorno:
    - Queda de tensão percentual (%ΔV) ou seção necessária (mm²)
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