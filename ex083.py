exp = input('Digite uma expressão: ')
lista = []
for parentese in exp:
    if parentese == '(':
        lista.append('(')
    elif parentese == ')':
        if len(parentese) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A sua expressão é valida!')
else:
    print('A sua expressão é inválida.')