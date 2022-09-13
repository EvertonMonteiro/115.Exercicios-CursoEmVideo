from time import sleep
import random
print(f'{"Vamos jogar pedra, papel e tesoura":=^40}')
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
esc1 = int(input('Escolha a sua opção: '))
esc2 = random.randint(1, 3)
print('Pedra...'), sleep(1)
print('Papel...'), sleep(1)
print('Tesoura!')
print('-='*18)
if esc1 == 1:
    print('O jogador escolheu Pedra.')
elif esc1 == 2:
    print('O jogador escolheu Papel.')
elif esc1 == 3:
    print('o jogador escolheu Tesoura.')
else:
    print('Você escolheu uma opção inválida, tente novamente. (seu burro)')
if esc2 == 1:
    print('O computador escolheu Pedra.')
elif esc2 == 2:
    print('O computador escolheu Papel.')
elif esc2 == 3:
    print('o computador escolheu Tesoura.')
print('-='*18)
if esc1 == esc2:
    print('Empate!')
elif esc1 == 1 and esc2 == 3 or esc1 == 2 and esc2 == 1 or esc1 == 3 and esc2 == 2:
    print('Você venceu!')
elif esc1 == 3 and esc2 == 1 or esc1 == 1 and esc2 == 2 or esc1 == 2 and esc2 == 3:
    print('O Computador venceu!')
else:
    print('Parabéns, você conseguiu estragar um programa simples.')

