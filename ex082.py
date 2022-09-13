lista = []
pares = []
impares = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    esc = input('Quer continuar [S/N] ? ').strip().lower()[0]
    if esc == 'n':
        break
print(f'''A lista completa é: {lista}
A lista de números pares é: {pares}
A lista de números impares é: {impares}''')

