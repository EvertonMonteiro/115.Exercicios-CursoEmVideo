def ajuda(fun):
    help(fun)


def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    comando = input('Função/Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)