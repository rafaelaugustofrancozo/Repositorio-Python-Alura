class conta_banco:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'Saldo da conta do titular {self.titular}: R${self.saldo}')

    def deposita(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} efetuado! Novo saldo: R${self.saldo}')

    def saca(self, valor):
        self.saldo -= valor
        print(f'Saque de R${valor} efetuado! Novo saldo: R${self.saldo}')

    def amplia_limite(self, valor):
        self.limite += valor
        print(f'Limite ampliado para R${self.limite}!')