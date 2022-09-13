distancia = float(input('Quantos km tem sua viagem? '))
if distancia <= 200:
    print(f'O preço da sua viagem foi R${distancia*0.5:.2f} levando em conta o valor de 50 centavos\npor km.')
else:
    print(f'O preço da sua viagem foi R${distancia*0.45:.2f} levando em conta o valor de 45 centavos\npor km.')
