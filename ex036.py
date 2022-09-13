from time import sleep
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Em quantos anos pretende pagar a casa? '))
parcela = casa / (anos*12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de {parcela:.2f}.')
print('Analisando...')
sleep(2)
if parcela > salario*0.30:
    print('O seu empréstimo foi negado!')
else:
    print('O seu empréstimo foi aprovado!')