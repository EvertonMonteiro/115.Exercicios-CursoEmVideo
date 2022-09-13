from random import randint
print('=-'*15, '\nVamos jogar PAR ou ÍMPAR\n', '=-'*15)
vitoria = 0
while True:
    n1 = int(input('Escolha um valor: '))
    n2 = randint(0, 10)
    esc = input('Par ou ímpar? [P/I] ').strip().upper()
    res = n1 + n2
    print('-'*30, f'\nVocê jogou {n1} e o computador jogou {n2}. O total equivale a {res}.\n','-'*30)
    if esc =='P':
        if res % 2 == 0:
            vitoria += 1
            print('''Você ganhou! \nVamos jogar mais uma vez :)''')
        else:
            print('''Você perdeu! HAHA''')
            break
    elif esc == 'I':
        if res % 2 == 1:
            vitoria += 1
            print('''Você ganhou! \nVamos jogar mais um vez :)''')
        else:
            print('Você perdeu! HAHA')
            break
    else:
        print('Você não escolheu par nem ímpar, tente novamente.')
print(f'FIM DE JOGO! Você venceu {vitoria} vezes.')






