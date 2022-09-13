adulto = homem = mulher = 0
while True:
    print('='*10, 'CADASTRE UMA PESSOA', '='*10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if idade >= 18:
        adulto += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    if cont == 'N':
        break
print(f'''O total de pessoas com mais de 18 anos é: {adulto}.
O total de homens cadastrados é: {homem}.
O total de mulheres com menos de 20 anos é: {mulher}.''')
