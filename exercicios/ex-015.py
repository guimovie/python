conta = []

class ContaBancaria:
    
    # Criando a classe Conta Bancaria e definindo os parâmetros
    def __init__(self, titular):
        self._titular = titular
        self._saldo = 0

    # Modo de visualização da Conta Bancaria
    def __str__(self):
        return f'Titular: {self._titular} | Saldo: R$ {self._saldo}'

def limpar():
    # Método para limpar o terminal
    print('\033c', end='')

def depositar():
    limpar()
    while True:
        entrada = input('Digite seu deposito: R$ ')
        try:
            valor = float(entrada.replace(',', '.'))
        except ValueError:
            limpar()
            print('Digite um valor numérico válido!')
            continue
        if valor <= 0:
            limpar()
            print('O depósito deve ser maior que zero!')
            continue
        break
    conta[0]._saldo += round(valor, 2)
    print('Saldo depositado!')
    input('Digite algo para voltar: ')
    menu()

def sacar():
    limpar()
    while True:
        entrada = input('Digite seu saque: R$ ')
        try:
            valor = float(entrada.replace(',', '.'))
        except ValueError:
            limpar()
            print('Digite um valor numérico válido!')
            continue
        if valor <= 0:
            limpar()
            print('O saque deve ser maior que zero!')
            continue
        break
    conta[0]._saldo -= round(valor, 2)
    print('valor sacado!')
    input('Digite algo para voltar: ')
    menu()

def extrato():
    limpar()
    print(f'Olá {conta[0]._titular}! seu Saldo atual é R$ {conta[0]._saldo}')
    input('Digite algo para voltar: ')
    menu()

def menu():
    # Menu principal
    limpar()

    print('=======================')
    print('|   Menu principal    |')
    print('=======================')
    print('1. Depositar')
    print('2. Sacar')
    print('3. Extrato')
    print('4. Sair')
    print('=======================')

    escolha = input('\n')
    
    match escolha:
        case '1': 
            depositar()
        case '2': 
            sacar()
        case '3': 
            extrato()
        case '4': 
            limpar()
            print('Saindo...')
        case _:
            print('Digite uma opção válida!')
            input('Digite algo para voltar: ')
            menu()



def main():
    # Cadastro do usuário e boas vindas
    limpar()
    print('=======================')
    print('|   Banco do Maxter   |')
    print('=======================')
    nome = input('Digite seu nome: ')
    perfil = ContaBancaria(nome)
    conta.append(perfil)
    print(f'Seja bem vindo {nome}!')
    input('Digite algo para ir ao menu: ')

    menu()

if __name__ == '__main__':
    main()