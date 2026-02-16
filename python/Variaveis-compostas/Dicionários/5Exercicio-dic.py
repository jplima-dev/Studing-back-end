def ini():
    print('-' *30)
ini()
print("PESSOAS")
ini()

tudo = []
dic = {}
media = []
mulheres = []
maior = []
while True:
    dic['nome'] = input("Nome: ")
    dic['idade'] = int(input("Idade: "))
    dic['sexo'] = input("(M, F)?: ").upper()
    
    if dic['sexo'] == 'F':
        mulheres.append(dic['nome'])
    tudo.append(dic.copy())
    media.append(dic['idade'])
    cont = input("Deseja continuar?(S/N): ").upper()
    
    if cont == 'N':
        break
coisa = sum(media) / len(media)
if dic['idade'] >= media:
    maior.append(dic['nome'])
ini()
print(f'{len(tudo)} pessoas foram cadastradas')
ini()
print(f'A media de idade e: {coisa}')
ini()
print("Mulheres cadastradas: ")
for m in mulheres:
    print(f' - {m}')
ini()
print(f'Pessoas com idade maior que a media: {maior}')
    
