def ini():
    print('-' *30)
    
ini()
print("APROVEITAMENTO DE JOGADOR")
ini()

jog = {}

jog['nome'] = input("digite o seu nome: ")
jog['partidas'] = int(input("qunatas partidas vc jogou?: "))
jog['gols'] = []
for i in range(0, jog['partidas']):
    gols_par = int(input(f'Quantos gols na partida {i + 1}?: '))
    jog['gols'].append(gols_par)
soma = sum(jog['gols'])
ini()
print(jog)
ini()
print(f'O jogador {jog["nome"]}, jogou {jog["partidas"]} partidas e fez {soma} gols no total')
ini()
print(f'O campo nome tem o valor: {jog["nome"]}')
print(f'O campo gols tem o valor: {jog["gols"]}')
print(f'o campo total tem o valor: {soma}')
ini()
print(f'O jogador {jog["nome"]}, jogou {jog["partidas"]} partidas.')
for i in range(0, jog["partidas"]):
    print(f'    => na partida {i + 1}, {jog["nome"]} fez {jog["gols"][i]} gols')