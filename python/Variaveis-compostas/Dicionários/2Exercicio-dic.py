import time
import random
from operator import itemgetter
jogadores = {'jogador1': random.randint(1, 6), 'jogador2': random.randint(1, 6), 'jogador3': random.randint(1, 6), 'jogador4': random.randint(1, 6)}
ranking = []
for d in jogadores:
    print(f'{d} = {jogadores[d]}')
    time.sleep(1)
print("Ranking dos jogadores")
ranking = sorted(jogadores.items(), key=itemgetter(1),  reverse = True)

for i, v in enumerate(ranking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}')