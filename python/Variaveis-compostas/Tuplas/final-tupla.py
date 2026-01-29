def ini():
    print('=-' *30)
    
ini()
print("TABELA DE PREÇOS")
ini()

produtos = ('arroz', 1.80, 'feijao', 2.30, 'carne', 35.50)

for i in range(0, len(produtos), 2):
    print(produtos[i], "R$", produtos[i + 1])