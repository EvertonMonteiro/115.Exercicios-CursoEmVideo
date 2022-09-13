termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
print(f'{termo} -> ', end='')
cont = 9
totcont = 1
while cont != 0:
    termo += razao
    cont -= 1
    totcont += 1
    print(f'{termo} -> ', end='')
    if cont == 0:
        print('PAUSA')
        cont = int(input('Quantos termos gostaria de adicionar a mais? '))
print(f'progressão foi finalizada com {totcont} termos mostrados.')