def opcoes():
    print('1. Verificador de Numero')
    print('2. Verificador de Idade')
    print('3. Login')
    print('4. Plano Cartesiano')

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

elif escolha_opcao == 3:
    usuario_correto = 'guimovie'
    senha_correta = 'senha123'
    
    usuario = input('USUARIO:')
    senha = input('SENHA:')

    if usuario == usuario_correto and senha == senha_correta:
        print('Acesso Permitido')
    else:
        print('ACESSO NEGADO!')

elif escolha_opcao == 4:
    print('VERIFICADOR DE QUADRANTE NO PLANO CARTESIANO')
    
    valor_x = float(input('DIGITE A COORDENDA X: '))
    valor_y = float(input('DIGITE A COORDENDA Y: '))

    if valor_x > 0 and valor_y > 0:
        print('Você está no Quadrante 1.')
    elif valor_x < 0 and valor_y > 0:
        print('Você está no Quadrante 2.')
    elif valor_x < 0 and valor_y < 0:
        print('Você está no Quadrante 3.')
    elif valor_x > 0 and valor_y < 0:
        print('Você está no Quadrante 4.')
    else:
        print('O ponto está localizado no Eixo ou Origem.')
