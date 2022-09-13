from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
for c in range(1, 5):
    jogo[f'jogador {c}'] = randint(1,6)
for key, value in jogo.items():
    print(f'O {key} jogou o dado e tirou: {value}')
    sleep(0.8)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos.')
    sleep(0.8)