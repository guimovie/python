class Restaurantes():
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._status = False
        Restaurantes.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.status}'

    @classmethod
    def listar_restaurantes(cls):
        print('\033c', end= '')
        print(f'\n{'NOME DO RESTAURANTE'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'STATUS'}')
        print('-' * 75)
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.status}')
        print()

    @property
    def status(self):
        return 'Ativo' if self._status else 'Desativado'

    def alternar_estado(self):
        self._status = not self._status


restaurante1 = Restaurantes('Pizza Planet', 'Fast Food')
restaurante1.alternar_estado()
restaurante2 = Restaurantes('Ligeirinhos', 'Hamburguer')
restaurante3 = Restaurantes('Comida da vovó', 'Caseiro')
restaurante4 = Restaurantes('Burguer King', 'Hamburguer')

Restaurantes.listar_restaurantes()

'''
print(restaurante1)
print(restaurante2)
'''