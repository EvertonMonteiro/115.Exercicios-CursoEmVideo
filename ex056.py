somaidade = 0
homemvelho = 0
nomevelho = ''
totmulher = 0
for c in range(1, 5):
     print(f'----{c}ª PESSOA----')
     nome = input('Nome: ').strip()
     idade = int(input('Idade: '))
     sexo = input('Sexo (M/F): ').upper().strip()
     somaidade += idade
     if sexo == 'M' and idade > homemvelho:
          homemvelho = idade
          nomevelho = nome
     if sexo == 'F' and idade < 20:
          totmulher += 1
print(f'''A média de idade do grupo é de {somaidade/4}.
O homem mais velho do grupo tem {homemvelho} anos e se chama {nomevelho}.
Ao total são {totmulher} com menos de 20 anos no grupo.''')



