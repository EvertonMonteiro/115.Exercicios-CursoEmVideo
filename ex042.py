n1 = int(input('Digite o valor do primeiro segmento: '))
n2 = int(input('Digite o valor do segundo segmento: '))
n3 = int(input('Digite o valor do terceiro segmento: '))
if n1+n2 > n3 and n1+n3 > n2 and n3+n2 > n1:
    print('Os segmentos podem formar um triângulo ', end='')
    if n1 == n2 == n3:
        print('equilátero.')
    if n1 == n2 or n1 == n3 or n2 == n3:
        print('isósceles.')
    else:
        print('escaleno.')
else:
    print('Os segmentos acima não podem formar um triângulo.')


