class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._status = False

    def __str__(self):
        return f'Titular: {self._titular} | Saldo: R$ {self._saldo} | Status: {self.status}'
        
    @property
    def titular(self):
        return self._titular
        
    @property
    def saldo(self):
        return self._saldo

    @property
    def status(self):
        return 'Ativado' if self._status else 'Desativado'    
        
    def alternar_status(self):
        self._status = not self._status
        
class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")

print(cliente1)
print(cliente2)
print(cliente3)