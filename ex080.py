lista = []
for c in range (1, 6):
    n = int(input('Digite um número: '))
    if c == 1 or n >= lista[-1]:
        lista.append(n)
        print('Esse valor foi adicionado ao final da lista.')
    elif n <= lista[0]:
        lista.insert(0, n)
        print('Esse valor foi adicionado a posição 0 da lista.')
    elif n <= lista[1]:
        lista.insert(1, n)
        print('Esse valor foi adicionado a posição 1 da lista.')
    elif n <= lista[2]:
        lista.insert(2, n)
        print('Esse valor foi adicionado a posição 2 da lista.')
    elif n <= lista[3]:
        lista.insert(3, n)
        print('Esse valor foi adicionado a posição 3 da lista.')
print(f'Os valores digitados em ordem foram: {lista}')