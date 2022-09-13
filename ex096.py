def area(largura, comprimento):
    area = largura * comprimento
    print(f'Um terreno {largura}x{comprimento} equivale a {area}m²!.')


print('Controle de Terrenos')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
