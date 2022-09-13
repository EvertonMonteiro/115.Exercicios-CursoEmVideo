n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print(f'Tirando {n1} e {n2} a sua média será {media}.')
if media < 5:
    print('Você foi reprovado!')
elif media >= 7:
    print('Parabéns, você foi aprovado!')
else:
    print('Você está de recuperação!')
