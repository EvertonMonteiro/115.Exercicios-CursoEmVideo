def ficha(nome='<desconhecido>', gol = 0):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = '0'
    print(f'O jogador {nome} fez {gol} gol(s)!')


jogador = input('Nome do jogador: ').strip()
gols = input('Número de Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
print(ficha(jogador, gols))