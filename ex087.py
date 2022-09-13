matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = coluna3 = linha2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            totpar += matriz[l][c]
        if c == 2:
            coluna3 += matriz[l][c]
        if l == 1:
            if c == 0:
                linha2 = matriz[l][c]
            elif matriz[l][c] > linha2:
                linha2 = matriz[l][c]
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print('-='*30)
print(f'A soma de todos os valores pares inseridos é: {totpar}.')
print(f'A soma dos valores da terceira coluna é:: {coluna3}')
print(f'O maior valor da segunda linha é: {linha2}')