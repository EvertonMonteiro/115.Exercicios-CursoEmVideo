from datetime import date
adulto = 0
jovem = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = date.today().year - ano
    if idade < 18:
        adulto += 1
    else:
        jovem += 1
print(f'Ao todo tivemos {adulto} pessoas adultas e {jovem} pessoas jovens')



