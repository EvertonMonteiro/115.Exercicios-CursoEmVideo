print('='*20)
print(f'{"BANCO BESSA":^20}')
print('='*20)
valor = float(input('Qual valor você deseja sacar? R$ '))
while valor != 0:
    if valor // 2 == 1:
        break
    cedula50 = valor // 50
    valor = valor - ( cedula50 * 50)
    print(f'Total de {cedula50:.0f} cédulas de R$50')
    cedula20 = valor // 20
    valor = valor - (cedula20 * 20)
    print(f'Total de {cedula20:.0f} cédulas de R$20')
    cedula10 = valor // 10
    valor = valor - (cedula10 * 10)
    print(f'Total de {cedula10:.0f} cédulas de R$10')
    cedula1 = valor
    valor = valor - cedula1
    print(f'Total de {cedula1:.0f} cédulas de R$1')
print('='*20)
print('Volte sempre! Tenha um ótimo dia!')
print('='*20)



