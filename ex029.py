vel = int(input('Qual velocidade você esta dirigindo ? '))
if vel > 80:
    print('Você foi multado pois excedeu o limite de velocidade (80km)')
    print(f'O Valor da sua multa é R${(vel-80)*7}')
print('Tenha um ótimo dia e dirija com segurança')
