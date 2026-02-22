# importando bibliotecas

import requests
from deep_translator import GoogleTranslator


# Chave API própria do OpenWeather
API_KEY = "API-KEY"

# input pra cidade

city = input("Cidade: ") 

# Criando o tradutor : GoogleTranslator (idioma de naturalidade, idioma de traducao) - Ingles -> Portugues
tradutor = GoogleTranslator(source="en", target="pt")
# API call para parametro (cidade)

link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
# Requisição get
requisicao = requests.get(link)
# Resultado do get em json 
call = requisicao.json()

# Variaveis visualizaveis
descricao = call['weather'][0]['description']

# temperatura vem em Kelvin (K), passe para Celcius usando a formula: C°: K - 273,15
temperatura = call['main']['temp'] - 273.15
# Umidade do ar em porcentagem
umidade_ar = call['main']['humidity']
# Print
# Texto traduzido
descricao_traduzida = tradutor.translate(descricao)

print(f'{city}, Descrição: {descricao_traduzida}, Temperatura: {round(temperatura, 2)} C°, Umidade do Ar: {umidade_ar}%')
