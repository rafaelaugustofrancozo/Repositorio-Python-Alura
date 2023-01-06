class conta_banco:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo da conta do titular {self.__titular}: R${self.__saldo}')

    def podesacar(self, valor_a_ser_sacado):
        limite_saque = self.__saldo + self.__limite
        return valor_a_ser_sacado < limite_saque #return vai retornar true or false, true apenas quando a condição do return for verdadeira


    def saca(self, valor):
        if self.__podesacar(valor): #pode parecer que falta condição, mas apenas declarando o if dessa forma,
            self.__saldo -= valor   #é como se disséssemos: se a podesacar, passando esse valor, retornar truem deduz o saldo, seria algo do tipo "if self.__podesacar(valor) is true"
            print(f'Saque de R${valor} efetuado! Novo saldo: R${self.__saldo}')
        else:
            print(f'O valor {valor} não pode ser sacado, pois estoura o limite da conta')

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

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

