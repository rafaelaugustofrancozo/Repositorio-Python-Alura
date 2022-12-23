from classe_conta import conta_banco
from datas import data

d = data(2, 11, 1988)
print(d.formatadata())

num = 2
print(type(num))

def amplia_limite():
    opcao = str(input('Deseja ampliar o limite da conta? S/N ')).strip().upper()
    if opcao == 'S':
        valor = float(input('Qual o valor? '))
        conta2.amplia_limite(valor)

conta2 = conta_banco(123, "Rafael", 1500.0, 2000.0)
print(conta2.saldo)
conta2.deposita(350.0)
conta2.saca(350.0)
conta2.extrato()
amplia_limite()



