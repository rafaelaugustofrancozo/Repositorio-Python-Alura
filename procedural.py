def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print(f'O saldo é {conta["saldo"]}!')


conta = criar_conta(123, "Rafael", 1500.0, 2000.0)
print(conta)
deposita(conta, 10000.0)
print(extrato(conta))