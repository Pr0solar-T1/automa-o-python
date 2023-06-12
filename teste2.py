import requests as r

response = r.get('https://rickandmortyapi.com/api/character')

if response.status_code == 200:
    data = response.json()

    if 'results' in data and len(data['results']) > 0:
        first_return = data['results'][0]

        valor = first_return['name']

        print(valor)

    else:
        print('se vira, deu erro')
else:
    print('esse erro é pior, se vira',response.status_code)

