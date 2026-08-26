# listagem de números
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('LISTA DE NÚMEROS: ')
for n in numero:
    print(f'-{n}')

# soma dos números ímpares
resultado = 0
for n in numero:
    if n % 2 != 0:
        resultado = resultado + n
print(f'\nSOMA DOS ÍMPARES: {resultado}\n')

# números de forma decrescente
print('NUMEROS EM DECRESCENTE: ')
for n in reversed(numero):
    print(f'-{n}')

# listagem de nomes
nomes = ['Guilherme', 'Claudio', 'Fernando', 'Cesar']
print('\nLISTA DE NOMES: ')
for nome in nomes:
    print(f'-{nome}')

# listagem de anos
anos = [2002, 2026]
print('\nLISTA DE ANOS: ')
for ano in anos:
    print(f'- {ano}')

# tabuada
print('\n--TABUADA--')
tabuada = int(input('Escolha um número: '))

for n in numero:
    print(f'{tabuada} X {n} = {tabuada * n}')

# soma dos elementos
lista = [10, 50, 30, 37, 28, 51, 69]
soma = 0
try:
    for n in lista:
        soma += n
        print(f'A soma da lista deu: {soma}')
except Exception as e:
    print(f'Erro na soma: {e}')

# média dos elementos
try:
    media = soma / len(lista)
    print(f'A média da lista é: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possivel calcular')
except Exception as e:
    print(f'Erro no calculo: {e}')