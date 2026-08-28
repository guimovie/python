restaurantes = [{'nome': 'VIP Sushi', 'categoria': 'Japonesa', 'status': False},
                {'nome': 'Zé do Hamburguer', 'categoria': 'Hamburguer', 'status': True},
                {'nome': 'Bullguer', 'categoria': 'Hamburguer', 'status': False}]

def exibir_nome_do_programa():
    #print('Sabor Express\n')
    print(''' 
    --------------------------------------------------------------------------
    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀ 
    --------------------------------------------------------------------------
    ''')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Status do Restaurante')
    print('4. Sair\n')

def voltar_ao_menu():
    input('\nDigite qualquer tecla para voltar ao menu principal: ')
    main()

def exibir_titulo(texto):
    print('\033c', end = '')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    exibir_titulo('Finalizando app.')

def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    exibir_titulo('CADASTRO DE NOVOS RESTAURANTES')
    nome_do_restaurante = input('Coloque o nome do restaurante q deseja cadastrar: ')
    categoria = input(f'Coloque a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'status': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_titulo('LISTA DOS RESTAURANTES')

    print(f'{'Nome do Restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Status' )

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'Disponível' if restaurante['status'] else 'Indisponível'
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status.ljust(20)}')

    voltar_ao_menu()

def status():
    exibir_titulo('ALTERANDO O STATUS DO RESTAURANTE')
    nome_restaurante = input('Digite o nome do restaurante q deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['status'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

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
            status()
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