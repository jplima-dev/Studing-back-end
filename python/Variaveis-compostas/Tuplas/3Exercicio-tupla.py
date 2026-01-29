import random

def ini():
    print('-=' *30)
    
ini()
print("NUMEROS ALEATORIOS TUPLAS")
ini()

numeros = (
                        random.randint(1, 10),
                        random.randint(1, 10),
                        random.randint(1, 10),
                        random.randint(1, 10),
                        random.randint(1, 10)
)

maior = numeros[0]
menor = numeros[0]

for i in numeros:
    print(f'numero: {i}')   
ini()

for a in numeros:
    if a > maior:
        maior = a
    if a < menor:
        menor = a
        
print(f'maior numero: {maior}')
print(f'menor numero: {menor}')