print(f'{"10 Termos de uma PA":=^40}')
termo = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão: '))
print(f'{termo:.0f} ->', end=' ')
for c in range(1, 11):
    termo+= razao
    print(f'{termo:.0f}', end=' -> ')
print('Acabou :)')