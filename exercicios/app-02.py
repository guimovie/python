from modelos.restaurantes import Restaurantes

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

def main():
    Restaurantes.listar_restaurantes()

if __name__ == '__main__':
    main()