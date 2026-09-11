class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao.title()

    def __str__(self):
        return f'Nome: {self._nome} | Idade: {self._idade} anos | Profissão: {self._profissao}'

    @property
    def saldacao(self):
        return f'Olá, meu nome é {self._nome}! Trabalho como {self._profissao}' if self._profissao else f'Olá, meu nome é {self._nome}!'
    
    def aniversario(self):
        self._idade += 1


pessoa1 = Pessoa('Guilherme', 24, 'Desenvolvedor')
pessoa1.aniversario()

print(pessoa1)
print(pessoa1.saldacao)