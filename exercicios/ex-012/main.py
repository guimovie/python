from veiculos import Veiculo
from carro import Carro
from moto import Moto

carro1 = Carro('Chevrollet', 'Celta', 2)
carro2 = Carro('Volkswagen', 'Gol', 4)
carro3 = Carro('Toyota', 'Corolla', 4)

carro1.virar_chave()

moto1 = Moto('Honda', 'Pop-100', 'Casual')
moto2 = Moto('Honda', 'CB-500', 'Casual')
moto3 = Moto('Yamaha', 'MT-09', 'Esportiva')

moto1.virar_chave()

print(carro1)
print(carro2)
print(carro3)
print(moto1)
print(moto2)
print(moto3)