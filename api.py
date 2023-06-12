import requests as r
import pandas as pd

import time as t


response = r.get(f'https://rickandmortyapi.com/api/character')

arq = 'planilha.xlsx'
arq1 = 'teste.xlsx'
planilha = 'Sheet1'

tabela = pd.read_excel(arq1, 'Planilha1')

tb = pd.ExcelFile(arq)
print(tb.sheet_names)
print(tabela)

pergunta = 0
count = 0

valores = {
    'Nome': [],
    'Status': [],
    'Especie': [],
    'Origem': [],
}

def buscar(item):
    if response.status_code == 200:
        data = response.json()
        # print(len(data['results']))

        if 'results' in data and len(data['results']) > 0:
            nome_item = data['results'][item]
            status_item = data['results'][item]
            especie_item = data['results'][item]
            origin_item = data['results'][item]

            nome = nome_item['name']
            status = status_item['status']
            especie = especie_item['species']
            origin = origin_item['origin']['name']

            valores['Nome'].append(nome)
            valores['Status'].append(status)
            valores['Especie'].append(especie)
            valores['Origem'].append(origin)


            print(nome, status)

            tabela_atualizada = tabela._append(pd.DataFrame(valores), ignore_index=True)
            print(tabela_atualizada)
            tabela_atualizada.to_excel('./planilhas/planilha3.xlsx')


    


while count < 19:
    count+=1
    pergunta+=1
    buscar(pergunta)


def atualizacao():
    for v in valores:
        tabela.loc[:, f'{v}'] = valores[f'{v}']
    tabela.to_excel('./planilhas/planilha5.xlsx')
    print(tabela)






continuar = input('Deseja atualizar a tabela? [s/n] ')

match continuar:
    case 's':
        print('processando...')
        t.sleep(5)

        while True:
            atualizacao()
            t.sleep(5)



    case 'n':
        print('ok')
    case _:
        print('Digite um valor valido!')

# def att():
    
    




# while True:
#     att()
#     t.sleep(60)


# print(tb)
