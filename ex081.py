lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    esc = input('Quer continuar [S/N] ? ').strip().lower()[0]
    if esc == 'n':
        break
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente equivalem a: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não foi encontrado na lista.')