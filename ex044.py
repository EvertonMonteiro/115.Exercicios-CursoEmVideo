print(f'{"Lojas Tabajara":=^40}')
valor = float(input('Digite o valor das compras: '))
print('''[ 1 ] À vista no dinheiro/cheque.
[ 2 ] À vista no cartão.
[ 3 ] Até 2x no cartão.
[ 4 ] 3x ou mais no cartão.''')
pag = int(input('Selecione o método de pagamento: '))
if pag == 1:
    print(f'A sua compra de {valor:.2f} vai custar R${valor*0.90:.2f}.')
elif pag == 2:
    print(f'A sua compra de {valor:.2f} vai custar R${valor*0.95:.2f}.')
elif pag == 3:
    print(f'''A sua compra será parcelada em 2x de R${valor/2:.2f} 
totalizando R${valor:.2f} no final.''')
elif pag == 4:
    parcela = int(input('Quantas parcelas? '))
    print(f'''Sua compra sera parcelada em {parcela}x de R${valor*1.20/parcela:.2f} com juros.
Sua compra de R${valor:.2f} vai custar um total de R${valor*1.20:.2f}''')
else:
    print('Você digitou um valor inválido.')
