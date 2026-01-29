def ini():
    print('-=' *30)
    
ini()
print("NUMEROS NA TUPLA")
ini()

pares = []
nove = 0
numeros = []
for i in range(1,5):
    numero = int(input("digite um numero: "))
    numeros.append(numero)
    
    if numero == 9:
        nove += 1
    
    if numero % 2 == 0:
        pares.append(numero)
    
    
    
ini()
print("quantidade de 9: ", nove)
tupla = tuple(numeros)
pos = tupla.index(3)
print(f'o numero 3 esta na {pos} posicao')
print(f'numeros pares: {pares}')

print(tupla)
