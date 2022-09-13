frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = juntar[::-1]
print(f'O inverso de {juntar} é {inverso}.')
if inverso == juntar:
    print('Temos um palíndromo.')
else:
    print('Não é um palíndromo.')


