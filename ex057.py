sexo = input('Digite o seu sexo (M/F): ').strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos, Digite seu sexo corretamente (M/F): ').strip().upper()
print(f'Sexo {sexo} foi registrado corretamente!')