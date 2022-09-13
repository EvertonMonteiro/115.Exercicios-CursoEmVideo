from random import randint
from time import sleep
jogo = []
print('-'*30)
print(f'{"JOGA NA MEGASENA":^30}')
print('-'*30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(F'=-=-=- SORTEANDO {n} JOGOS -=-=-=')
for c in range(1, n+1):
    print(f'Jogo {c}: ', end='')
    for sorteio in range(0, 6):
        jogo.append(randint(1, 99))
    print(jogo)
    jogo.clear()
    sleep(1)
print('-'*30)