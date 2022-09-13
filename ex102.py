def fatorial(n, show = False):
    '''
    --> Função para Fatoriação de números!
    :param n: Número para ser fatoriado
    :param show: Mostrar o cálculo
    :return: Resultado do cálculo fatorial do número N
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, True))