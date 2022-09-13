num = int(input('Digite um número inteiro: '))
print('''Agora escolha uma base para ser feita a conversão:
1. Converter para Binário
2. Converter para Octal
3. Converter para hexadecimal''')
escolha = int(input('Qual opção você deseja? '))
if escolha == 1:
    print(f'{num} convertido para binário equivale a {bin(num)[2:]}.')
elif escolha == 2:
    print(f'{num} convertido para octal equivale a {oct(num)[2:]}.')
elif escolha == 3:
    print(f'{num} convertido para hexadecimal equivale a {hex(num)[2:]}.')
else:
    print('Você digitou um valor inválido :/')