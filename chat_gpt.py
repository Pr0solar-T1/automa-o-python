import requests as r
import pandas as pd

response = r.get('https://rickandmortyapi.com/api/character')

arq = 'planilha.xlsx'
planilha = 'Sheet1'

def ler_planilha():
    return pd.read_excel(arq, sheet_name=planilha)

tb = ler_planilha()

print(tb)

def buscar(item):
    if response.status_code == 200:
        data = response.json()

        if 'results' in data and len(data['results']) > 0:
            item_data = data['results'][item]

            nome = item_data['name']
            status = item_data['status']

            print(nome, status)

            if planilha in tb:
                tb.insert(2, 'name',[nome, status], True)
            else:
                print('Coluna não encontrada!')

            tb.to_excel(arq, sheet_name=planilha, index=False)  # Salva o DataFrame atualizado no arquivo
            print(tb)

        else:
            print('Não foram encontrados resultados.')
    else:
        print('Erro na requisição:', response.status_code)

print(tb)

pergunta = int(input('Digite o ID que você deseja puxar: '))

buscar(pergunta)