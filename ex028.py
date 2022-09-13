import random
print('Vamos jogar um jogo :)')
lista = [0, 1, 2, 3, 4, 5]
escolha = random.choice(lista)
num = int(input('Digite um número inteiro entre 0 e 5: '))
if num == escolha:
    print(f'Parabéns! Você acertou :), eu tinha pensando no número {escolha}')
else:
    print(f'Você errou :/, eu tinha pensado no número {escolha} e você digitou {num}')
print('-----FIM-----')