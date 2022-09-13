from datetime import date
ano = int(input('Em qual ano você nasceu? '))
idade = date.today().year - ano
print(f'Quem nasceu em {ano} tem {idade} anos.')
if idade <= 9:
    print('Você é considerado um atleta mirim.')
elif idade <= 14:
    print('Você é considerado um atleta infantil.')
elif idade <= 19:
    print('Você é considerado um atleta junior.')
elif idade <= 25:
    print('Você é considerado um atleta sênior.')
else:
    print('Você é considerado um atleta master.')
