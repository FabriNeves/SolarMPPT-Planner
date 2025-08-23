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

def buscaValorMaior(valorProcurado,lista):
  valor = 0
  indice =0
  for i,val in enumerate(lista):
    if val >= valorProcurado:
      valor = val
      indice = i
      break
  return [valor,indice]

resultado = buscaValorMaior(250,metodosB1["3_condutores_carregados"])
secao = metodosB1['Secao_nominal_mm2'][resultado[1]]
print(f"Seção Nominal: {secao} mm²")

djComerciais = [10,16,20,25,32,40,50,63,70,80,100,125,150,175,200,225]

def buscaValorMenor(valorProcurado,lista):
  valor = 0
  indice = 0
  for i,val in enumerate(lista):
    if val <= valorProcurado:
      if i == 0:
        valor = val
        indice = i
      elif val > valorProcurado:
        valor = lista[i-1]
        indice = i-1
  return [valor,indice]

