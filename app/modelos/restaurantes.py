from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurantes():
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        Restaurantes.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.status}'

    @classmethod
    def listar_restaurantes(cls):
        print('\033c', end= '')
        print(f'\n{'NOME DO RESTAURANTE'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'AVALIAÇÕES'.ljust(25)} |{'STATUS'}')
        print('-' * 100)
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.status}')
        print()

    @property
    def status(self):
        return 'Ativo' if self._status else 'Desativado'

    def alternar_estado(self):
        self._status = not self._status

    def receber_nota(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        num_de_avaliacoes = len(self._avaliacao)
        media = round(soma_das_notas / num_de_avaliacoes, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)