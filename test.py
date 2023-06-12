import requests as r
response = r.get('https://rickandmortyapi.com/api/character')

print(response)

if response.status_code == 200:
    data = response.json()

    print(data.get('id'))

    if isinstance(data['results'], list):
        valor= data.get('name')

        print(valor)
    
    else:
        print('n é uma lista, boa sorte')
else:
    print('erro, pensa mais', response.status_code)
