import cmath
import math

def calcular_correntes_aprimorado(tensao_linha_V, lista_potencias):
    """
    Calcula as correntes de linha (IA, IB, IC) e de fase (IAB, IBC, ICA)
    em um sistema trifásico com base nas potências e conexões das cargas.
    Valida se as fases correspondem ao número de fases.

    Args:
        tensao_linha_V (float): A tensão de linha em Volts.
        lista_potencias (list): Uma lista de dicionários com potência, fases e nfases.

    Returns:
        tuple: Uma tupla com as correntes fasoriais (IA, IB, IC, IAB, IBC, ICA).
    """

    # Inicializar as correntes de fase (para cargas monofásicas em triângulo)
    I_fase_AB_total = 0 + 0j
    I_fase_BC_total = 0 + 0j
    I_fase_CA_total = 0 + 0j

    # Inicializar as correntes de linha (a soma total)
    I_linha_A_total = 0 + 0j
    I_linha_B_total = 0 + 0j
    I_linha_C_total = 0 + 0j

    for carga in lista_potencias:
        potencia = carga["pot"]
        fases = carga["fases"].upper()
        num_fases = carga["nfases"]

        # 1. Validação de Dados: Verifica se a especificação da fase corresponde ao número de fases
        if (num_fases == 2 and fases not in ["AB", "BC", "CA"]) or \
           (num_fases == 3 and fases != "ABC"):
            print(f"AVISO: A carga com fases '{fases}' e {num_fases} fases não é válida. Será ignorada.")
            continue

        if num_fases == 2:
            # Calcular a magnitude da corrente para cargas monofásicas
            corrente_mag = potencia / tensao_linha_V

            if fases == "AB":
                # A corrente de fase I_AB é a referência com 0 graus
                I_fase_AB_total += cmath.rect(corrente_mag, math.radians(0))
            elif fases == "BC":
                # A corrente de fase I_BC está defasada 120 graus
                I_fase_BC_total += cmath.rect(corrente_mag, math.radians(120))
            elif fases == "CA":
                # A corrente de fase I_CA está defasada -120 graus
                I_fase_CA_total += cmath.rect(corrente_mag, math.radians(-120))

        elif num_fases == 3:
            # Calcular a corrente de linha para cargas trifásicas
            corrente_mag = potencia / (math.sqrt(3) * tensao_linha_V)

            # As correntes de linha são adicionadas diretamente às correntes de linha totais
            I_linha_A_total += cmath.rect(corrente_mag, math.radians(0))
            I_linha_B_total += cmath.rect(corrente_mag, math.radians(120))
            I_linha_C_total += cmath.rect(corrente_mag, math.radians(-120))

    # As correntes de linha totais são a soma fasorial das correntes
    # das cargas trifásicas mais a contribuição das cargas monofásicas.
    # O cálculo (I_fase_AB_total - I_fase_CA_total) representa a soma
    # vetorial das correntes de fase em cada nó, conforme a Lei de Kirchhoff.
    IA_final = I_linha_A_total + (I_fase_AB_total - I_fase_CA_total)
    IB_final = I_linha_B_total + (I_fase_BC_total - I_fase_AB_total)
    IC_final = I_linha_C_total + (I_fase_CA_total - I_fase_BC_total)

    return IA_final, IB_final, IC_final, I_fase_AB_total, I_fase_BC_total, I_fase_CA_total

# Exemplo de uso com uma lista de N cargas, incluindo uma inválida
tensao_linha = 220
cargas_complexas = [
    {"pot": 2200, "fases": "AB", "nfases": 2},
    {"pot": 4400, "fases": "BC", "nfases": 2},
    {"pot": 8800, "fases": "CA", "nfases": 2},
    {"pot": 10000, "fases": "ABC", "nfases": 3}
]

IA, IB, IC, IAB, IBC, ICA = calcular_correntes_aprimorado(tensao_linha, cargas_complexas)

# Exibindo os resultados em forma retangular e polar
print("--- Correntes de Linha ---")
print(f"Corrente IA: {IA:.2f} A, Polar: {abs(IA):.2f} A < {math.degrees(cmath.phase(IA)):.2f}°")
print(f"Corrente IB: {IB:.2f} A, Polar: {abs(IB):.2f} A < {math.degrees(cmath.phase(IB)):.2f}°")
print(f"Corrente IC: {IC:.2f} A, Polar: {abs(IC):.2f} A < {math.degrees(cmath.phase(IC)):.2f}°\n")

print("--- Correntes de Fase (Monofásicas) ---")
print(f"Corrente IAB: {IAB:.2f} A, Polar: {abs(IAB):.2f} A < {math.degrees(cmath.phase(IAB)):.2f}°")
print(f"Corrente IBC: {IBC:.2f} A, Polar: {abs(IBC):.2f} A < {math.degrees(cmath.phase(IBC)):.2f}°")
print(f"Corrente ICA: {ICA:.2f} A, Polar: {abs(ICA):.2f} A < {math.degrees(cmath.phase(ICA)):.2f}°")