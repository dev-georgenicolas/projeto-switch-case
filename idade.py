import datetime

anoNasc = int(input("Em que ano você nasceu? "))
mesNasc = int(input("Em que mês você nasceu? "))
diaNasc = int(input("Em que dia você nasceu? "))

dataNasc = datetime.date(anoNasc, mesNasc, diaNasc)
dataAtual = datetime.date.today()

idade = dataAtual.year - dataNasc.year
if dataNasc.month > dataAtual.month or (dataNasc.month == dataAtual.month and dataNasc.day > dataAtual.day):
    idade -= 1
    
meses = (dataAtual.year - dataNasc.year) * 12 + dataAtual.month - dataNasc.month
dias = (dataAtual - dataNasc).days
semanas = dias // 7
print(f"Idade: {idade} anos, {meses} meses, {dias} dias, {semanas} semanas")