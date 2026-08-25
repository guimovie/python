restaurantes = []

def exibir_nome_do_programa():
    #print('Sabor Express\n')
    print(''' 
    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀ 
    ''')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def voltar_ao_menu():
    input('\nDigite qualquer tecla para voltar ao menu principal: ')
    main()

def exibir_titulo(texto):
    print('\033c', end = '')
    print(texto)
    print()

def finalizar_app():
    exibir_titulo('Finalizando app.')

def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    exibir_titulo('CADASTRO DE NOVOS RESTAURANTES')
    nome_do_restaurante = input('Coloque o nome do restaurante q deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_titulo('LISTA DOS RESTAURANTES')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        # ou vc pode usar => opcao_escolhida = int(opcao_escolhida)
        #print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    print('\033c', end = '')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()