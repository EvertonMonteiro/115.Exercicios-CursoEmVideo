lista = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n in lista:
        print('Esse valor ja foi adicionado anteriormente, digite outro.')
    else:
        print('Valor Adicionado com sucesso!')
        lista.append(n)
    esc = input('Gostaria de adicionar outro número [S/N] ? ').strip().lower()[0]
    if esc == 'n':
        break
print('=-'*30)
print('A sua lista ficou assim: ')
print(f'{sorted(lista)}')