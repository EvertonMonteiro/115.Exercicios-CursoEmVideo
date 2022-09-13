dados = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    dados.append([nome, [n1, n2], media])
    esc = input('Quer continuar [S/N] ? ').strip().lower()[0]
    if esc != 's' and esc != 'n':
        esc = input('Opção inválida, Quer continuar [S/N] ? ')
    if esc == 'n':
        break
print('-='*30)
print(f'{"No":<3}  {"Nome":<10}     {"Média":>6}')
print('-='*30)
for i, a in enumerate(dados):
    print(f'{i:<3}  {a[0]:<10}    {a[2]:>6.2f}')
print('-='*30)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    if aluno <= len(dados)-1:
        print(f'O aluno(a) {dados[aluno][0]} tirou as notas: {dados[aluno][1]}')

