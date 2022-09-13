salario = float(input('Digite o valor do seu salário: '))
if salario >1250:
    print(f'Seu salário recebeu um acréscimo de 15%, agora você ganha R${(salario*0.10)+salario:.2f}.')
if salario <=1250:
    print(f'Seu salário recebeu um acréscimo de 10%, agora você ganha  R${(salario*0.15)+salario:.2f}.')
print('Parabéns, continue o bom trabalho!')