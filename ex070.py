print('='*10, 'LOJAS TABAJARA', '='*10)
totprod = totvalor = valorbarato = valorcaro = 0
prodbarato = ''
while True:
    totprod += 1
    prod = input('Nome do produto: ').strip()
    valor = float(input('Preço do produto: R$ '))
    cont = ' '
    while cont not in 'SN':
       cont = input('Quer continuar? [S/N' ).strip().upper()[0]
    totvalor += valor
    if totprod == 1 or valor < valorbarato:
        prodbarato = prod
        valorbarato = valor
    if valor >= 1000:
        valorcaro += 1
    if cont == 'N':
        break
print(f'''O total da compra equivale a R${totvalor:.2f}.
Temos {valorcaro} produto(s) custando mais de R$1000.00.
O produto mais barato foi {prodbarato} que custa R${valorbarato:.2f}.
VOLTE SEMPRE :)''')





