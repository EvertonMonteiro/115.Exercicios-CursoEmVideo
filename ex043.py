peso = float(input('Quanto você pesa? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / altura**2
print(f'Seu imc é {imc:.1f},', end='')
if imc < 18.5:
    print('você está abaixo do peso.')
elif imc < 25:
    print ('você está no peso ideal.')
elif imc < 30:
    print('você está com sobrepeso.')
elif imc < 40:
    print('você está obeso.')
else:
    print('você está com obesidade mórbida.')
