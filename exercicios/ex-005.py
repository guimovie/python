class Musica():
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Snuff'
musica1.artista = 'Slipknot'
musica1.duracao = 300

musica2 = Musica()
musica2.nome = 'Bohemian Rhapsody'
musica2.artista = 'Queen'
musica2.duracao = 330 

print(vars(musica1))
print(dir(musica1))