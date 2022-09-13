resp = 'S'
maior = menor = totnum = soma = 0
while resp == 'S':
    totnum += 1
    num = int(input('Digite um número: '))
    if totnum == 1:
        num = maior = menor
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    soma += num
    resp = input('Deseja Continuar? [S/N] ').strip().upper()
print(f'''Você digitou {totnum} números e a média foi {soma/totnum}.
O maior valor inserido foi {maior} e o menor foi {menor}.''')


