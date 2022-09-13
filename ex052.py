n = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        total += 1
if total == 1 or total == 2:
    print(f'O número {n} é um número primo!')
else: print(f'O número {n} não é um número primo.')
