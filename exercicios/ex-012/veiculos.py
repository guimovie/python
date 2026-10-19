class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False
    def __str__(self):
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'Seu veículo: {self._modelo.ljust(15)} | Marca: {self._marca.ljust(15)} | está {status.ljust(10)}'

    def virar_chave(self):
        self._ligado = not self._ligado