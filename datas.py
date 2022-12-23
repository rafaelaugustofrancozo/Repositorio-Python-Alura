import datetime


class data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatadata(self):
        dataformatada = str(self.dia)+'/'+str(self.mes)+'/'+str(self.ano)
        return dataformatada