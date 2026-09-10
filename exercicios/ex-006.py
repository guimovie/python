class Restaurantes():
    nome = ''
    categoria = ''
    status = False
# restaurante 1
restaurante1 = Restaurantes()
restaurante1.nome = 'Praça'
restaurante1.categoria = 'Italiana'

# restaurante 2
restaurante2 = Restaurantes()
restaurante2.nome = 'Pizza Place'
restaurante2.categoria = 'Fast Food'
restaurante2.status = True

nome_do_restaurante1 = restaurante1.nome
categoria = Restaurantes.categoria
restaurante1.nome = 'Bistrô'

print(nome_do_restaurante1)
print(restaurante1.status)
print(f'Restaurante {restaurante1.nome} está Ativo!' if restaurante1.status else f'Restaurante {restaurante1.nome} está Inativo!\n')
print(restaurante2.nome)
print(restaurante2.categoria)
print(f'A categoria do restaurante {restaurante2.nome} é Fast Food' if restaurante2.categoria == 'Fast Food' else f'A categoria do restaurante {restaurante2.nome} não é Fast Food')


'''
if restaurante1.status:
    print(f'Restaurante {restaurante1.nome} está Ativo!')
else:
    print(f'Restaurante {restaurante1.nome} está Inativo!')
'''
