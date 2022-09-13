n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou {n}.')
print(f'O valor 9 apareceu {n.count(9)} vezes!')
if 3 in n:
     print(f'O primeiro número 3 apareceu na {n.index(3) + 1}ª posição.')
else:
     print('O número 3 não apareceu nenhuma vez.')
print('Os valores pares inseridos foram: ', end='')
for numero in n:
     if numero % 2 == 0:
          print(numero, end='')