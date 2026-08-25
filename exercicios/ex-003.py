numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('LISTA DE NÚMEROS: ')
for n in numero:
    print(f'-{n}')
resultado = 0
for n in numero:
    if n % 2 != 0:
        resultado = resultado + n

print(f'\nSOMA DOS ÍMPARES: {resultado}')

nomes = ['Guilherme', 'Claudio', 'Fernando', 'Cesar']
print('\nLISTA DE NOMES: ')
for nome in nomes:
    print(f'-{nome}')

anos = [2002, 2026]
print('\nLISTA DE ANOS: ')
for ano in anos:
    print(f'- {ano}')