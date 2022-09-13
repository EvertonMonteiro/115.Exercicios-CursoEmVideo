def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO! {entrada} não é um valor válido.')
        else:
            válido = True
            return float(entrada)