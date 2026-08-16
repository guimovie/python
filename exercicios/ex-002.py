def opcoes():
    print('1. Verificador de Numero')
    print('2. Verificador de Idade')

opcoes()

escolha_opcao = int(input('Escolha uma opção: '))

if escolha_opcao == 1:
    print('VERIFICADOR DE NÚMERO')
    par_impar = int(input('Digite o numero: '))

    if par_impar%2 == 0:
        print(f'O numero {par_impar} é PAR!')
    else:
        print(f'O numero {par_impar} é IMPAR!')

elif escolha_opcao == 2:
    print('VERIFICADOR DE IDADE')
    idade = int(input('Digite sua Idade: '))

    if idade < 13:
        print('Você é um(a) CRIANÇA')
    elif idade >= 13 and idade < 18:
        print('Você é um(a) ADOLECENTE')
    if idade >= 18:
        print('Você é um(a) ADULTO')

def main():
    opcoes()

if __name__ == '__main__':
    main()