n = tot = soma = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    tot += 1
print(f'A soma dos valores {tot} digitados equivale a {soma}.')
