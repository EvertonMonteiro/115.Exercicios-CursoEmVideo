c = 0
fatorial = 1
n = int(input('Digite um número inteiro para calcular o seu fatorial: '))
for c in range (1, n):
    fatorial *= n
    n -=1
print(f'A fatorial do número inserido equivale a {fatorial}.')
