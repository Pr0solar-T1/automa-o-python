import requests as r
import pandas as pd

import time as t
import json as j




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
    # 'Status': [],
    'Especie': [],
    'Origem': [],
}

def buscar(item):

    link = 'https://teste-api-593aa-default-rtdb.firebaseio.com/'

    response = r.get(f'{link}.json')
    
    if response.status_code == 200:
        data = response.json()
        # dados = j.dumps(data)
        # print(dados)

        if 'item' in data and len(data['item']) > 0:
            nome_item = data['item'][item]
            # status_item = data['item'][item]
            especie_item = data['item'][item]
            origin_item = data['item'][item]

            nome = nome_item['name']
            # status = status_item['status']
            especie = especie_item['specie']
            origin = origin_item['origin']['name']

            valores['Nome'].append(nome)
            # valores['Status'].append(status)
            valores['Especie'].append(especie)
            valores['Origem'].append(origin)


            # print(nome, status)
            print(nome,especie,origin)

            tabela_atualizada = tabela._append(pd.DataFrame(valores), ignore_index=True)
            print(tabela_atualizada)
            tabela_atualizada.to_excel('./planilhas/planilha3.xlsx')


while count < 3:
    count+=1
    pergunta+=1
    buscar(pergunta)


def atualizacao():

    while True:
        for v in valores:
            tabela.loc[:, f'{v}'] = valores[f'{v}']
            # print(valores[f'{v}'])
            print(tabela)
        tabela.to_excel('./planilhas/planilha4.xlsx')
    # print(tabela)
    #     response_atualizado = r.get(f'{link}.json')
    #     print(response.text)
    #     t.sleep(5)
    # # if response.status_code == 200:
    # #     data = response.json()
    # #     # print(data)
    # #     if 'item' in data:
    # #         print(data['item'])
    #     # print(data)
    #     # print(data['item'])
    #     # print('---------')

    #     # for d in data['item']:
    #     #     print(d)







continuar = input('Deseja atualizar a tabela? [s/n] ')

match continuar:
    case 's':
        print(valores)
        print('processando...')
        t.sleep(5)

        while True:
            atualizacao()
            t.sleep(5)



    case 'n':
        print('ok')
    case _:
        print('Digite um valor valido!')

