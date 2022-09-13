def maior(*num):
    print('-='*20)
    print('Analisando os valores inseridos...')
    if len(num) == 0:
        print('Não foi inserido nenhum valor...')
    else:
        print(f'Números informados: {num} | Foram informados {len(num)} valores ao todo.')
        print(f'O maior número encontrado foi {max(num)}!')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
