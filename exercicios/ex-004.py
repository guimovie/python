print('\033c', end = '')

# dicionário de informações
info = {'nome': 'Guilherme', 'idade': '23', 'cidade': 'Barueri'}

info['idade'] = '24'
info['profissão'] = 'DEV'
del info['cidade']
for i in info:
    print(f'{i}: {info[i]}')

# verificação de informações
verific_info = input('\nDigite uma informação que deseja verificar: ')
if verific_info in info:
    print(f'Informação encontrada! {info[verific_info]}\n')
else:
    print('Informação não encontrada!\n')
    
# dicionário de número
num = {x: x**2 for x in range(1, 7)}
for n in num:
    print(f'{n} ao quadrado é {num[n]}')

# contagem de palavras
frase = "A casa é bonita, e quando falo dessa casa eu me lembro de quando era jovem, me lembro de ter uma sala bonita e um jardim mais ou menos."
print(frase)
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    print(f'{palavra}: {contagem_palavras[palavra]}')