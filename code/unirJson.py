import json
import os
#unifica os json gerados pelas diferentes requests à API
# Diretório onde estão os arquivos JSON
diretorio = "dados"  # Substitua pelo caminho real

# Lista para armazenar todos os itens de "data"
dados_combinados = []

# Percorre todos os arquivos no diretório
for arquivo in os.listdir(diretorio):
    if arquivo.endswith(".json"):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            # Adiciona os itens de "data" à lista combinada
            dados_combinados.extend(dados["data"])

# Cria o novo JSON combinado
json_final = {"data": dados_combinados}

# Salva o resultado em um novo arquivo
with open("tweets.json", "w", encoding="utf-8") as f:
    json.dump(json_final, f, ensure_ascii=False, indent=4)

print("Arquivos JSON combinados com sucesso em 'tweets.json'!")