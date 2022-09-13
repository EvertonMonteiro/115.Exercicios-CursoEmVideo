from random import randint
def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Sorteando 5 números...\nOs números sorteados foram: {lista}')
def somapar(listanum):
    totpar = 0
    for v in listanum:
        if v % 2 == 0:
            totpar += v
    print(f'Somando os valores pares de {listanum}...\nA soma equivale a {totpar}.')


lista = list()
sorteia(lista)
somapar(lista)