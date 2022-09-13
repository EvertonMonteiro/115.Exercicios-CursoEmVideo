def voto(ano):
    from datetime import date
    idade =  date.today().year - ano
    if idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    if idade < 18:
        print(f'Com {idade} anos: NÃO VOTA.')
    if idade >= 65 or 16 <= idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL.')


print('-'*20)
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)