class Musica():
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def lista_musicas():
        print('---LISTAGEM DE MÚSICAS---\n')
        for m in Musica.musicas:
            print(f'Nome: {m.nome}')
            print(f'Artista: {m.artista}')
            print(f'Duração: {m.duracao}s\n')
    
musica1 = Musica('Snuff', 'Slipknot', 300)
musica2 = Musica('Bohemian Rhapsody', 'Queen', 330 )
musica3 = Musica('Chicago', 'Michael Jackson', 320 )
musica4 = Musica('Confortably Numb', 'Pink Floyd', 430 )

Musica.lista_musicas()