import requests
#Consultor de CPF

cep = input('Digíte seu CEP: ')
url = f'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' in dados:
        print('CEP não encontrado')
    else:
        print(f'Logradouro: {dados.get('logradouro')}')
        print(f'Bairro: {dados.get('bairro')}')
        print(f'Cidade-UF: {dados.get('localidade')}-{dados.get('uf')}')
else:
    print('Erro ao conectar a API')