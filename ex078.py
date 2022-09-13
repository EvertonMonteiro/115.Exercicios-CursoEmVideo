lista = []
posimaior = []
posimenor = []
for c in range (0, 5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))
maior = max(lista)
menor = min(lista)
for p in range (len(lista)):
    if lista[p] == maior:
        posimaior.append(p)
    if lista[p] == menor:
        posimenor.append(p)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi: {maior} e foi inserido na posição {posimaior}')
print(f'O maior valor digitado foi: {menor} e foi inserido na posição {posimenor}')