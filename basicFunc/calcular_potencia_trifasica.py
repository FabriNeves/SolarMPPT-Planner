import math

def calcular_potencia_trifasica(n_fases, tensao_linha, corrente, cos_fi=1):
  """
  Calcula a potência elétrica com base no número de fases.
  Valida o número de fases no intervalo [1, 3] e o fator de potência no intervalo [0.8, 1.0].
  """
  p = 0

  # Validação do número de fases
  if n_fases < 1 or n_fases > 3:
    print(f"Erro: Número de fases ({n_fases}) fora do intervalo válido [1, 3].")
    return 0

  # Validação do Fator de Potência (cos φ)
  # A forma "if not (0.8 <= cos_fi <= 1.0):" é uma maneira Pythonica de verificar o intervalo.
  if cos_fi < 0.8 or cos_fi > 1.0:
    print(f"Erro: Fator de potência ({cos_fi}) fora do intervalo válido [0.8, 1.0].")
    return 0

  # Se as validações passaram, executa o cálculo
  match n_fases:
    case 1:
      #print("Cálculo para sistema Monofásico:")
      # Em sistemas monofásicos e bifásicos, usa-se a Tensão de Fase.
      # V_fase = V_linha / sqrt(3) em um sistema trifásico equilibrado.
      tensao_fase = tensao_linha / math.sqrt(3)
      p = tensao_fase * corrente * cos_fi
    case 2:
      #print("Cálculo para sistema Bifásico (fase-fase):")
      # A tensão entre duas fases é a própria tensão de linha.
      p = tensao_linha * corrente * cos_fi
    case 3:
      #print("Cálculo para sistema Trifásico:")
      p = tensao_linha * math.sqrt(3) * corrente * cos_fi

  return p

# --- Exemplo --- #
'''
- Disjuntor de 40A
- Tensão de Linha : 220V
- Numero de fases : 3
- Fator de Potencia : 1.0(Padrão)
 '''
calcular_potencia_trifasica(n_fases=3, tensao_linha=220, corrente=40)

print(calcular_potencia_trifasica(n_fases=3, tensao_linha=220, corrente=40))

