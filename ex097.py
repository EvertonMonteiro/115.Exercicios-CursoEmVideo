def escreva(texto):
    tamanho = len(texto) + 4
    print(f'~'*tamanho)
    print(f'{texto:^{tamanho}}')
    print(f'~'*tamanho)
escreva('Everton')
escreva('Sou um homem afortunado e devo buscar minha fortuna.')
escreva('SIC PARVIS MAGNA')