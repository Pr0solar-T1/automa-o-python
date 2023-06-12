import requests as r
import pandas as pd

import time as t
# import json as j

arq = 'teste.xlsx'
planilha = 'Sheet1'

tabela = pd.read_excel(arq, 'Planilha1')


valores = {
    'id':[],
    'nome': [],
    'specie': [],
    'origin': [],
}
valores_att = {
    'id':[],
    'nome': [],
    'specie': [],
    'origin': [],
}

def buscar():
    link = 'https://teste-api-593aa-default-rtdb.firebaseio.com/'

    response = r.get(f'{link}.json')

    if response.status_code == 200:
        data = response.json()

        if 'item' in data and len(data['item']) > 0:
            # print(len(data['item']))
            quant = 0

            while quant < len(data['item']) - 1:
                quant +=1
                id_item = data['item'][quant]['id']
                name_item = data['item'][quant]['name']
                specie_item = data['item'][quant]['specie']
                origin_item = data['item'][quant]['origin']['name']
                # print(id_item,specie_item,origin_item)

                valores['id'].append(id_item)
                valores['nome'].append(name_item)
                valores['origin'].append(origin_item)
                valores['specie'].append(specie_item)

                tabela_atualizada = tabela._append(pd.DataFrame(valores), ignore_index=True)
                print(tabela_atualizada)
                tabela_atualizada.to_excel('./planilhas/planilha6.xlsx')
                

buscar()



continuar = input('Deseja atualizar a tabela? [s/n] ')

match continuar:
    case 's':
        print(valores)
        print('processando...')
        t.sleep(5)

        while True:
            buscar()
            t.sleep(5)



    case 'n':
        print('ok')
    case _:
        print('Digite um valor valido!')