class Livro:
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._disponivel = True

    def __str__(self):
        return f'Titulo: {self._titulo.ljust(20)} | Autor: {self._autor.ljust(20)} | Ano: {self._ano.ljust(10)} | Disponibilidade: {self._disponivel}'

    def emprestar(self):
        self._disponivel = False

livro1 = Livro('Diario de Anne Frank', 'Annie Frank', '1945')
livro2 = Livro('Manual de Fulano', 'Fulano', '2000')
livro1.emprestar()

print(livro1)
print(livro2)