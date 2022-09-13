from random import randint
num = randint(1, 10)
totpalpite = 1
print('''Olá! Vamos jogar um jogo ?
Acabei de pensar em um número de 1 a 10.
Agora você precisa adivinhar qual foi :)''')
palpite = int(input('Qual o seu palpite? '))
while palpite != num:
    totpalpite += 1
    if palpite > num:
        print('Eu pensei em um número menor, tente de novo!')
        palpite = int(input('Qual o seu palpite? '))
    if palpite < num:
        print('Eu pensei em um número maior, tente de novo!')
        palpite = int(input('Qual o seu palpite? '))
print(f'Parabéns! Você acertou com {totpalpite} tentativas :).')
