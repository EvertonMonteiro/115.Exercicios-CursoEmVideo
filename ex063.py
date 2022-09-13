print(f'{"Sequência de Fibonacci":=^40}')
n = int(input('Digite a quantidade de termos que você deseja: '))
n2 = 0
cont = 0
n3 = 1
if n <= 0:
    print('Opção inválida, tente novamente.')
elif n == 1:
    print('0 -> ', end='')
elif n == 2:
    print('0 -> 1 -> ', end='')
else:
    print('0 -> 1 -> ', end='')
    while cont < n - 2 :
     n1 = n2
     n2 = n3
     n3 += n1
     cont += 1
     print(f'{n3} -> ', end='')
print('FIM')