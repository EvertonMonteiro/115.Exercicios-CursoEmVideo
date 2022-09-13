from time import sleep
def contador(i, f, p):
    print('-=' * 20)
    print(f'A contagem de {i} até {f} de {p} em {p}:')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > f:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont -= p
        print('Fim!')
    else:
        cont = i
        while cont <= f:
            sleep(0.4)
            print(f'{cont} ', end='')
            cont += p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
