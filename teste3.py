import requests as r
import json

link = 'https://teste-api-593aa-default-rtdb.firebaseio.com/'

response = r.get(f'{link}.json')

print(response)
print(response.text)

valores = {
    'id': [],
    'name': [],
    'status': []
}

# if response.status_code == 200:
#     data = response.json()
    
#     print(data['results']['name'])

#     if 'results' in data:
#         id = data['results']['id']
#         name = data['results']['name']
#         status = data['results']['status']

#         print(id,name,status)

#         valores['id'].append(id)
#         valores['name'].append(name)
#         valores['status'].append(status)


# print(valores)

def buscar(item):
    if response.status_code == 200:
        data = response.json()

        # print(len(data))

        if 'results' in data and len(data) > 0:
            items = data['item'][item]
            print(items['name'])
            # for v in valores:
                
                # valores[v].append(items)

            # id_item = data['results']
            # print(len(data['results']))
            # print(id_item[item])
            # print(id_item)
            # print(valores)

pergunta = int(input('digite um id: '))
buscar(pergunta)
