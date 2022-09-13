dados = dict()
lista = list()
totidade = idadecont = totpessoas = 0
while True:
    dados['nome'] = input('Nome: ')
    totpessoas += 1
    sexo = input('Sexo [M/F]:  ').strip().upper()[0]
    while True:
        if sexo in 'MF':
            break
        else:
            sexo = input('Valor inválido! Sexo [M/F]: ').strip().upper()[0]
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    totidade += dados['idade']
    idadecont += 1
    lista.append(dados.copy())
    resp = input('Quer continuar [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
    if resp != 'S' and resp != 'N':
        resp = (input('Valor inválido! Quer continuar? [S/N] '))
media = totidade / totpessoas
print('-='*30)
print(f'Ao todo temos {totpessoas} pessoas cadastradas.')
print(f'A média de idade é de {media} anos.')
print('A lista de mulheres cadastradas é:')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end='')
print('Lista de pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'| {k} = {v} |', end='')
        print()
