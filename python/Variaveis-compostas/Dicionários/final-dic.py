def ini():
    print('-' * 30)

ini()
print("APROVEITAMENTO DE JOGADOR 2.0")
ini()

tudo = []

while True:
    jogador = {}
    gols_lista = []

    jogador['nome'] = input("Nome: ")
    jogador['partidas'] = int(input("Quantas partidas?: "))

    for i in range(jogador['partidas']):
        gols = int(input(f'Quantos gols na partida {i + 1}: '))
        gols_lista.append(gols)

    jogador['gols'] = gols_lista
    jogador['total'] = sum(gols_lista)

    tudo.append(jogador.copy())

    cont = input("Continuar(S/N)?: ").upper()
    if cont == 'N':
        break

print("\nResumo:")
for j in tudo:
    print(j)