n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opt = 0
while opt != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior número
[ 4 ] Escolher novos números
[ 5 ] Sair do programa''')
    opt = int(input('>Qual é a sua opção ? '))
    if opt == 1:
        print(f'A soma entre {n1} e {n2} equivale a {n1+n2}.')
        opt = int(input('>Qual é a sua opção ? '))
    if opt == 2:
        print(f'A multiplicação entre {n1} e {n2} equivale a {n1*n2}.')
        opt = int(input('>Qual é a sua opção ? '))
    if opt == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é o {n1}.')
        elif n2 > n1:
            print(f'O maior número entre {n1} e {n2} é o {n2}.')
        else:
            print('Os valores são iguais!')
        opt = int(input('>Qual é a sua opção ? '))
    if opt == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('''[ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior número
        [ 4 ] Escolher novos números
        [ 5 ] Sair do programa''')
        opt = int(input('>Qual é a sua opção ? '))
    else:
        print('Você digitou um valor inválido.')
    print('=-='*10)
print('Acabou :)')