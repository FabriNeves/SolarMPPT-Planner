from datetime import datetime
import math

# --- Funções "Esqueleto" (Stubs) para a Lógica do Projeto ---
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
  # A forma "if not (0.8 <= cos_fi <= 1.0):"
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


def gerarTitulo(potencia_inversor_kw, qtd_inversor=1):
  """Gera o título do projeto com base na potência total dos inversores."""
  potencia_total = potencia_inversor_kw * qtd_inversor
  print(f"LOG: Gerando título para {potencia_total} kW...")
  # Lógica a ser implementada:
  return f"PROJETO SISTEMA FOTOVOLTAICO {potencia_total:.2f} kW"

def gerarNomeProjeto(n_projeto, potencia_inversor_kw):
  """Gera um nome ou código para o desenho/arquivo do projeto."""
  print(f"LOG: Gerando nome do desenho para o projeto {n_projeto}...")
  # Lógica a ser implementada:
  return f"{n_projeto}-{potencia_inversor_kw}kW"

def dataHoje():
  """Retorna a data atual formatada."""
  # Esta função já tem a lógica final.
  return datetime.now().strftime('%d/%m/%Y')

def textoPolos(n_fases):
  """Retorna o texto do número de polos (ex: 'Bipolar', 'Tripolar')."""
  print(f"LOG: Definindo polos para {n_fases} fases...")
  # Lógica a ser implementada:
  if n_fases == 1:
    return "Monopolar"
  elif n_fases == 2:
    return "Bipolar"
  elif n_fases == 3:
    return "Tripolar"
  return "N/A"

def selecionarDisjuntorInversor(corrente_max_inversor):
  """Seleciona o disjuntor apropriado com base na corrente do inversor."""
  print(f"LOG: Selecionando disjuntor para {corrente_max_inversor}A...")
  # Lógica a ser implementada (ex: consulta a um DB de disjuntores):
  return "Disjuntor de XX A" # Placeholder

def selecionarTerra(cabo_fase_mm2):
  """Seleciona a bitola do cabo de aterramento com base no cabo fase."""
  print(f"LOG: Selecionando cabo de terra para um cabo fase de {cabo_fase_mm2} mm²...")
  # Lógica a ser implementada (conforme norma NBR 5410):
  return "Cabo de XX mm²" # Placeholder

def gerarTextoTotalModulos(qtd_modulos, potencia_modulo_wp):
    """Gera o texto descritivo da quantidade e potência dos módulos."""
    print(f"LOG: Gerando texto para {qtd_modulos} módulos de {potencia_modulo_wp}Wp...")
    # Lógica a ser implementada:
    return f"{qtd_modulos} MÓDULOS DE {potencia_modulo_wp}Wp"

def gerarTextoProtecaoGeral(texto_polos, disjuntor_entrada):
  """Gera o texto descritivo para a proteção CA geral."""
  print(f"LOG: Gerando texto da proteção CA...")
  # Lógica a ser implementada:
  return f"DISJUNTOR {texto_polos.upper()} {disjuntor_entrada}"


# --- ESTRUTURAÇÃO DO DICIONÁRIO 'NovoProjeto' ---

# 1. Defina as variáveis de entrada do seu projeto
# (Estes seriam os dados que você coleta do cliente ou dos equipamentos)
potencia_inversor_kw = 4.6
quantidade_inversores = 1
endereco_cliente = "Rua Teste, 123, Cidade Exemplo"
n_projeto = "FV2025-001"
n_art = "987654321"
nome_cliente = "Empresa Fictícia LTDA"
disjuntor_entrada = 63
n_fases_entrada = 3
tensao_linha = 220
concessionaria = "ENEL-RJ"
corrente_max_inversor = 20.9 # Exemplo, viria do datasheet do inversor
cabo_fase_selecionado_mm2 = 6 # Exemplo, viria de outra função
qtd_modulos_total = 10
potencia_modulo_wp = 550 # Exemplo, viria do datasheet do módulo
m_inversor = {"modelo": "ABC-4.6K-G2", "potMax": 4600} # Exemplo
m_modulo = {"modelo": "XYZ-550W", "potMax": 550} # Exemplo
nome_resp_tec = "Fulano de Tal"
registro_resp_tec = "CREA-RJ 123456/D"


# 2. Crie o dicionário chamando as funções
NovoProjeto = {
    "Título": gerarTitulo(potencia_inversor_kw, quantidade_inversores),
    "Endereço": endereco_cliente,
    "Projeto": n_projeto,
    "Desenho": gerarNomeProjeto(n_projeto, potencia_inversor_kw),
    "Data": dataHoje(),
    "ART": n_art,
    "Cliente": nome_cliente,
    "Disjuntor de Entrada": disjuntor_entrada,
    "Numero de Fases": n_fases_entrada,
    "Polos": textoPolos(n_fases_entrada),
    "Tensão de Linha": tensao_linha,
    "PotMaxProjeto": calcular_potencia_trifasica(n_fases_entrada, tensao_linha,disjuntor_entrada),
    "Concessionária": concessionaria,
    "Disjuntor Inversor": selecionarDisjuntorInversor(corrente_max_inversor),
    "Terra Inversor": selecionarTerra(cabo_fase_selecionado_mm2),
    "Geradores": [{
        "Modelo Inversor": m_inversor["modelo"],
        "Qtd Inversor": quantidade_inversores,
        "Modelo Modulo": m_modulo["modelo"],
        "Qtd Modulo": qtd_modulos_total
    }],
    "Inversor com proteção integrada": gerarTextoTotalModulos(qtd_modulos_total, m_modulo["potMax"]),
    "Proteção CA 220V String Box AC": gerarTextoProtecaoGeral(textoPolos(n_fases_entrada), disjuntor_entrada),
    "Resp.Tec": nome_resp_tec,
    "Registro do Responsável": registro_resp_tec
}

# 3. Imprima o resultado final para visualização
import pprint
pprint.pprint(NovoProjeto)