from datetime import datetime
dic = {}

dic['nome'] = input("Digite o seu nome: ")
nasc = int(input("Digite seu ano de nasc: "))
dic['idade'] = datetime.now().year - nasc
dic['clt'] = int(input("Carteira de trabalho(0 não tem): "))
if dic['clt'] != 0:
    dic['contra'] = int(input("Ano de contratação: "))
    dic['salario'] = float(input("Salario: R$ "))
    dic['aposentadoria'] =  dic['idade'] + ((dic['contra'] + 35) - datetime.now().year)

for k, v in dic.items():
    print(f'  - {k} tem o valor {v}')
