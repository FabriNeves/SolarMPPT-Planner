import math

# Tabela de diâmetro externo dos cabos (simplificado, com isolação PVC)
diametros_cabos = {
    1.5: 3.0,
    2.5: 4.5,
    4: 5.0,
    6: 6.5,
    10: 8.0,
    16: 9.5,
    25: 11.5,
    35: 13.0,
    50: 15.0,
    70: 17.5,
    95: 20.0
}

# Tabela de eletrodutos e suas áreas internas (mm²)
eletrodutos = {
    "1/2\"": 84,
    "3/4\"": 145,
    "1\"": 254,
    "1 1/4\"": 461,
    "1 1/2\"": 684,
    "2\"": 887,
     "2 1/2\"":1146,
    "3\"": 1538,
    "4\"":2606,
}


def area_cabo(diametro_mm):
    raio = diametro_mm / 2
    return math.pi * raio ** 2

def fator_ocupacao(qtd_cabos):
    if qtd_cabos <= 3:
        return 0.53
    elif qtd_cabos <= 6:
        return 0.40
    else:
        return 0.33

def dimensionar_eletroduto(cabos):
    """
    Parâmetro `cabos` deve ser uma lista de tuplas: [(bitola_mm2, quantidade), ...]
    """
    area_total_cabos = 0
    total_cabos = 0

    for bitola, qtd in cabos:
        if bitola not in diametros_cabos:
            raise ValueError(f"Bitola {bitola} mm² não está na tabela.")
        diametro = diametros_cabos[bitola]
        area = area_cabo(diametro)
        area_total_cabos += area * qtd
        total_cabos += qtd

    fator = fator_ocupacao(total_cabos)

    for nome, area_eletroduto in eletrodutos.items():
        if area_total_cabos <= area_eletroduto * fator:
            return {
                "eletroduto_recomendado": nome,
                "area_util": area_eletroduto,
                "ocupacao_usada": round(area_total_cabos / area_eletroduto * 100, 2)
            }

    return "Nenhum eletroduto padrão suporta esses cabos!"

