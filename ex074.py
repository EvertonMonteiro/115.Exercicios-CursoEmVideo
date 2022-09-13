from random import randint
valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
    randint(0, 10), randint(0, 10))
print(f'''Os valores selecionados foram:
{valores}
O maior valor selecionado foi: {max(valores)}.
O menor valor selecionado foi: {min(valores)}.''')