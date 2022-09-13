termo = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
cont = 0
print(f'{termo} -> ', end='')
while cont != 9:
    cont += 1
    termo += razao
    print(f'{termo} -> ', end='')
print('Fim')
