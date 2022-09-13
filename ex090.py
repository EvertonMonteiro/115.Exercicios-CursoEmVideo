aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['resultado'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['resultado'] = 'Recuperação'
else:
    aluno['resultado'] = 'Reprovado'
print('=-'*30)
for c, v in aluno.items():
    print(f'{c} = {v}')