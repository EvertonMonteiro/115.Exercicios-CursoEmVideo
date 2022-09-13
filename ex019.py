import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno ')
list = [a1, a2, a3]
ra = random.choice(list)
print(f'O aluno escolhido para limpar o quadro no fim da aula foi {ra}')
