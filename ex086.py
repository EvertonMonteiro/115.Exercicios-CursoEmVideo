lista = [[], [], [], [], [], [], [], [], []]
for c in range (0, 9):
        if c <= 2:
            lista[c].append(int(input(f'Digite um valor para [0, {c}]: ')))
        elif c <= 5:
            lista[c].append(int(input(f'Digite um valor para [1, {c-3}]: ')))
        elif c <= 9:
            lista[c].append(int(input(f'Digite um valor para [2, {c-6}]: ')))
for c in range (0, 9):
    print(f'{lista[c]}', end='')
    if c == 2 or c == 5 or c == 9:
        print()