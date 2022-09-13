jogador = dict()
gols = list()
dados = list()
while True:
    jogador['nome'] = input('Qual o nome do jogador? ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1 , partidas+1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    dados.append(jogador.copy())
    if resp not in 'SN':
        resp = input('Resposta Inválida! Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('-='*40)
print('Cod: ', end='')
for nome in jogador.keys():
    print(f'{nome:<15}', end='')
print()
print('-='*40)
for k, v in enumerate(dados):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if busca >= len(dados):
        print('Não existem jogadores com esse código de busca.')
        busca = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    else:
        print(f'Informações do jogador {dados[busca]["nome"]}:')
        for c in range(0, len(dados[busca]['gols'])):
            print(f' => Na partida {c+1}, fez {dados[busca]["gols"][c]} gols.')
print('Programa ENCERRADO!')
