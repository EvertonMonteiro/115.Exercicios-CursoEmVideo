n = int(input('Digite um número entre 1 e 9999: '))
print('Analisando o número inserido...')
print(f'A unidade do número inserido é: {n//1%10}')
print(f'A dezena do número inserido é: {n//10%10}')
print(f'A centena do número inserido é: {n//100%10}')
print(f'A milhar do número inserido é: {n//1000%10}')

