from datetime import date
cadastro = dict()
cadastro['Nome'] = input('Nome: ')
cadastro['Ano'] = int(input('Ano de Nascimento: '))
idade =  date.today().year - cadastro['Ano']
cadastro['CTPS'] = int(input('Carteira de Trabalho: '))
if cadastro['CTPS'] != 0:
    cadastro['Contrato'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Valor do Salário: R$'))
    cadastro['Aposentadoria'] = (35 + cadastro['Contrato']) - cadastro['Ano']
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}.')