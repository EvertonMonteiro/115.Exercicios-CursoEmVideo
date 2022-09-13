from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('Comparando números...')
sleep(2)
if n1 > n2:
    print(f'O maior número citado foi {n1}!')
elif n2 > n1:
    print(f'O maior número citado foi {n2}!')
else:
    print('Você digitou dois números iguais :|')

