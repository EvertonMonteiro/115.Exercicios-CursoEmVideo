from datetime import date
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
diferenca = 18 - idade
if diferenca == 0:
    print('Você esta na idade certa para se alistar, se apresente na junta militar mais próxima!')
elif diferenca >= 1:
    print(f'''Ainda falta {diferenca} ano(s) para o seu alistamento.
Seu alistamento será em {date.today().year+diferenca}.''')
else:
    print(f'''Você deveria ter se alistado há {diferenca*-1} anos.
Seu alistamento foi em {date.today().year+diferenca}.''')



