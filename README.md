# Algoritmo de Dados Climáticos

Este projeto é um algoritmo em Python que consulta o clima em tempo real a partir do nome de uma cidade.

Foram utilizadas:

* OpenWeather API para obter os dados climáticos
* Biblioteca deep-translator para traduzir as descrições do inglês para português

---

## Como executar

1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Crie um ambiente virtual

```bash
python -m venv venv
```

3. Ative o ambiente

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

4. Instale as dependências

```bash
pip install requests deep-translator
```

---

## Observação

Para executar o projeto, é necessário ter uma chave da OpenWeather.

Crie uma conta em: https://openweathermap.org/
Gere sua API Key e aguarde a ativação (pode levar algumas horas).
Depois, insira a chave no código onde indicado.
