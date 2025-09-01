import json

with open("database\\dataModules.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

for key in dados:
    print(key['model'])