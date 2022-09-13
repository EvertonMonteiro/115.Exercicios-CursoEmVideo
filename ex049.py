print(f'{"Tabuada v2":=^30}')
num = int(input('Digite um número inteiro para ver sua tabuada: '))
for c in range(1, 11,):
    print(f'{num} x {c:2} = {num*c}')