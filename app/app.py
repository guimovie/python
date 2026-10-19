from modelos.restaurantes import Restaurantes
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante1 = Restaurantes('Vip Sushi', 'Japonesa')
restaurante2 = Restaurantes('Zé do Hamburguer', 'Hamburguer')
restaurante3 = Restaurantes('Mania de Churrasco', 'Self Service')
restaurante4 = Restaurantes('Ké Coxinha', 'Salgados')

restaurante1.alternar_estado()
restaurante1.receber_nota('Guilherme', 10)
restaurante1.receber_nota('Flavio', 8)
restaurante1.receber_nota('Gustavo', 5)
restaurante1.receber_nota('Humberto', 7)
restaurante4.alternar_estado()
bebida_suco = Bebida('Suco de Melancia', 10, 'G')
prato_principal = Prato('Escargote no Buféte', 50, 'Comida chic')


def main():
    #Restaurantes.listar_restaurantes()
    print(bebida_suco, ',', prato_principal)

if __name__ == '__main__':
    main()