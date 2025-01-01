import os

# Defina a estrutura de pastas
directories = [
    "./templates",
    "./static"
]

files = [
    "./app.py",
    "./templates/index.html",
    "./static/style.css",
    "./requirements.txt"
]

# Criar diretórios
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Criar arquivos
for file in files:
    with open(file, 'w') as f:
        pass  # Apenas cria os arquivos vazios

print("Estrutura de pastas e arquivos criada com sucesso!")


# Gerado pelo ChatGPT adptado por min 
