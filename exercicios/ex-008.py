class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

meu_carro = Car('Fusca', 'Azul', 1970)

class Restaurante:
    def __init__(self, nome, categoria, status = False, capacidade = 0, estrelas = 0):
        self.nome = nome
        self.categoria = categoria
        self.status = status
        self.capacidade = capacidade
        self.estrelas = estrelas
    def __str__(self):
        return f'{self.nome} | Categoria: {self.categoria} | Status: {self.status} | Capacidade: {self.capacidade} pessoas | {self.estrelas} estrelas'

restaurante1 = Restaurante('Pizza Hut', 'Pizza', capacidade = 200, estrelas = 5)
restaurante2 = Restaurante('Bullguer', 'Hamburguer')

print(restaurante1)
print(restaurante2)

class Cliente:
    clientes = []
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        Cliente.clientes.append(self)
    def lista():
        print('---LISTA DE CLIENTES---')
        for c in Cliente.clientes:
            print(f'nome: {c.nome}')
            print(f'idade: {c.idade} anos')
            print(f'altura: {c.altura}m')
            print(f'peso: {c.peso}kg\n')
            

cliente1 = Cliente(nome = 'Guilherme', idade = '24', altura = '1.73', peso = '74')
cliente2 = Cliente(nome = 'Alexandre', idade = '15', altura = '1.72', peso = '58')
cliente3 = Cliente(nome = 'Fulano', idade = '50', altura = '2.00', peso = '90')

Cliente.lista()