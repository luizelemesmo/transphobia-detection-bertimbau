import json
import csv
from unidecode import unidecode
import re  # Importa o módulo para expressões regulares

# Função para limpar o texto: remove menções, links e espaços extras
def limpar_texto(texto):
    texto = re.sub(r'@\w+', '', texto)  # Remove menções como @username
    texto = re.sub(r'http\S+|www\S+', '', texto)  # Remove links como http://... ou www...
    texto = re.sub(r'\s+', ' ', texto).strip()  # Remove espaços extras e múltiplos espaços
    return texto

# Carrega o arquivo JSON
with open('ultimostts.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Lista para os dados ajustados
dados_ajustados = []

# Ajusta cada entrada
for item in dados['data']:
    id_item = item['id']
    texto_limpo = limpar_texto(item['text'])  # Limpa menções, links e espaços
    texto_final = unidecode(texto_limpo.replace('\n', ' '))  # Remove quebras de linha e acentos
    dados_ajustados.append({'id': id_item, 'text': texto_final})

# Gera o CSV com delimitador vírgula e aspas
with open('dados_ajustados.csv', 'w', encoding='utf-8', newline='') as f:
    escritor = csv.DictWriter(f, fieldnames=['id', 'text'], delimiter=';', quoting=csv.QUOTE_ALL)
    escritor.writeheader()  # Escreve o cabeçalho
    escritor.writerows(dados_ajustados)  # Escreve os dados

print("CSV gerado com sucesso em 'dados_ajustados.csv'!")