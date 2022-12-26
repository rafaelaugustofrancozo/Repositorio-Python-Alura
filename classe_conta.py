class conta_banco:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo da conta do titular {self.__titular}: R${self.__saldo}')

    def saca(self, valor):
        self.__saldo -= valor
        print(f'Saque de R${valor} efetuado! Novo saldo: R${self.__saldo}')

    def deposita(self, valor):
        self.__saldo += valor
        print(f'Depósito de R${valor} efetuado! Novo saldo: R${self.__saldo}')

    def amplia_limite(self, valor):
        self.__limite += valor
        print(f'Limite ampliado para R${self.__limite}!')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @limite.setter
    def limite(self, limite):
        self.__limite += limite

