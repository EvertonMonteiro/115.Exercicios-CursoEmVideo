from time import sleep
num = int(input('Digite um número inteiro: '))
print('Analisando seu número...')
sleep(2)
if num % 2 == 0:
    print('O número que você digitou é par!')
else:
    print('O número que você digitou é impar!')