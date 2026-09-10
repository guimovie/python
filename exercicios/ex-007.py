class Restaurantes():
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.status = False
        Restaurantes.restaurantes.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.status}'

    def listar_restaurantes():
        for restaurante in Restaurantes.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.status}')

restaurante1 = Restaurantes('Pizza Planet', 'Fast Food')
restaurante2 = Restaurantes('Ligeirinhos', 'Hamburguer')

Restaurantes.listar_restaurantes()
'''
print(restaurante1)
print(restaurante2)
'''