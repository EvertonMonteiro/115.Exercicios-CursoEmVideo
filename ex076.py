print('--'*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--'*20)
lista = ('Lápis', 1.75, 'Borracha', 2.50, 'Caderno', 16.20, 'Estojo', 27.80, 'Mochila', 150.50, 'Caneta', 1.50)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('--'*20)