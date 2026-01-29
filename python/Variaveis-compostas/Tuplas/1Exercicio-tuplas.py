def lin():
    print('-' *30)

lin()
print("NUMEROS POR EXTENSO")
lin()

numeros = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

usuario = int(input("digite um numero que queira ver por extenso: "))

if 1<= usuario <= 20:
    print(f'seu numero por extenso e: {numeros[usuario - 1]}')
else:
    print("numero invalido")