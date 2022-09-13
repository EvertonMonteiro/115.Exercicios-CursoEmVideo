temp = []
dados = []
maior = menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(dados) == 0:
      maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    dados.append(temp[:])
    temp.clear()
    esc = input('Quer continuar [S/N] ? ').strip().lower()[0]
    if esc != 'n' and esc != 's':
        esc = input('Opção Inválida! Quer continuar [S/N] ? ').strip().lower()[0]
    if esc == 'n':
        break
print(f'Foram cadastradas {len(dados)} pessoas!')
print(f'O maior peso cadastrado equivale a {maior}Kg e pertence a: ', end='')
for p in dados:
    if p[1] == maior:
        print(p[0])
print(f'O menor valor cadastrado equivale a {menor}Kg e pertence a: ', end='')
for p in dados:
    if p[1] == menor:
        print(p[0])