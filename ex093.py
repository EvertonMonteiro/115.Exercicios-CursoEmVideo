jogador = dict()
gols = list()
totgol = 0
jogador['nome'] = input('Qual o nome do jogador? ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1 , partidas+1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*30)
print(f'{jogador}')
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas. ')
for c in range(0, partidas):
    print(f'=> Na partida {c}, fez {gols[c]} gols.')
print(f'Foi um total de {jogador["total"]}.')