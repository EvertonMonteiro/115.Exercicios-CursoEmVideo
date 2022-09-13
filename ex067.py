n = 0
print(f'{"Tabuada V3":=^30}')
while n >= 0:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('=-='*30)
    for c in range (1, 11):
        print(f'{n} X {c:2} = {n*c}')
    print('=-='*30)
print('Acabou :)')
