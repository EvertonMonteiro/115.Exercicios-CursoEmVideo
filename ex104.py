def ler(num):
    num = input('Digite um número: ')
    while num.isnumeric() == False:
        print('ERRO! Digite um número válido')
        num = input('Digite um número: ')
    valor = int(num)
    return  valor

n = ler('Digite um número: ')
print(f'Você digitou o número {n}!')