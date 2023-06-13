import requests as r
import pandas as pd
import time as t
# import json as j

arq = 'teste.xlsx'
planilha = 'Sheet1'

tabela = pd.read_excel(arq, 'Planilha1')

#usado para armazenar os valores puxados da api em arrays
valores = {
    'id':[],
    'nome': [],
    'specie': [],
    'origin': [],
}
#função criada para buscar e puxar os valores da api
def buscar():
    #Link da api
    link = 'https://teste-api-593aa-default-rtdb.firebaseio.com/'

    response = r.get(f'{link}.json') #puxa a api

    #verifica se o status da api é 200 (caso ela esteja respondendo)
    if response.status_code == 200:
        #se a api respondeu, então ela transforma todos os valores em um JSON
        data = response.json()

        #verifica se tem a chave de nome "item" e se esse "item" é maior que zero (no caso, ve se tem algum valor)
        if 'item' in data and len(data['item']) > 0:
            #contador
            quant = 0

            #espolio de guerra, não ta servindo pra nada... ta ai pq vai que precise
            valores_atualizados = {
                'id':[],
                'nome': [],
                'specie': [],
                'origin': [],
            }

            #esse while serve para que o contador siga sempre a quantidade do JSON do "item" (serve para pegar as posições do array)
            while quant < len(data['item']) - 1:
                #inicia o contador
                quant +=1
                #aqui ele passa por cada posição do array e pega os valores dos "cabeça de chave"
                id_item = data['item'][quant]['id']
                name_item = data['item'][quant]['name']
                specie_item = data['item'][quant]['specie']
                origin_item = data['item'][quant]['origin']['name']
                # print(id_item,specie_item,origin_item)

                #envias os dados puxados da api para as chaves
                valores['id'].append(id_item)
                valores['nome'].append(name_item)
                valores['origin'].append(origin_item)
                valores['specie'].append(specie_item)                

                #aqui envia os valores da api que estão na variavel para dentro da planilha
                tabela_atualizada = tabela._append(pd.DataFrame(valores), ignore_index=True)
                #printa a planilha
                print(tabela_atualizada)
                #executa a planilha
                tabela_atualizada.to_excel('./planilhas/planilha6.xlsx')

#função cria para atualizar os valores da planilha
def att():
    #aqui ele limpa os arrays
    valores['id'].clear()
    valores['nome'].clear()
    valores['origin'].clear()
    valores['specie'].clear()
    #printa todos os valores para ver se limpou msm
    print(valores)

    #timer de 3 segundos até carregar a função "Buscar"
    t.sleep(3)
    #executa de uma maneira que atualiza os valores da planilha (sem deixar somar no array, mas sim, substituindo os valores)
    buscar()

#executa a função para fazer a primeira busca
buscar()

#Pergunta se o usuario deseja continuar
continuar = input('Deseja atualizar a tabela? [s/n] ')

#caso a resposta seja diferente das que estão logo abaixo ele cai num loop infinito até que o usuario digite certo
while continuar != 's' and continuar != 'n':
        print('Digite um valor valido!')
        continuar = input('Deseja atualizar a tabela? [s/n] ')

#caso o usuario digite certo, executa essa parte
match continuar:
    #caso o usuario digite "s"
    case 's':
        #mospra a mensagem processando e logo dps vem um timer de 5 segundos até executar a função de atualizar
        print('processando...')
        t.sleep(5)
        #é um loop infinito de atualização (atualiza a cada 100 segundos)
        while True:
            # buscar()
            #executa a função de atualizar infinitamente em um timer de 100 segundos (1m40s)
            att()
            t.sleep(100)


    #caso o usuario digite "n"
    case 'n':
        print('ok')

        
