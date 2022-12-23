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

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_saldo(self, saldo):
        self.__saldo += saldo

    def set_titular(self, titular):
        self.__titular = titular

    def set_limite(self, limite):
        self.__limite += limite