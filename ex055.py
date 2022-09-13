maiorp = 0
menorp = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if peso > maiorp:
        maiorp = peso
    if peso < menorp or menorp == 0:
        menorp = peso
print(f'''O maior peso inserido foi {maiorp}Kg. 
O menor peso inserido foi {menorp}Kg.''')
