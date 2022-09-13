lista = [[],[]]
print('Insira números inteiros!')
for c in range (1, 8):
    n = int(input(f'Digite o {c}o valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 == 1:
        lista[1].append(n)
print(f'''Os números pares inseridos foram: {lista[0]}.
Os números ímpares inseridos foram: {lista[1]}.''')