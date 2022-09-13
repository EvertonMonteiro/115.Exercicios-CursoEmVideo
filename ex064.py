totnum = num = 0
contnum = 0
while num != 999:
    num = int(input('Digite um número [Digite 999 para parar.]: '))
    if num != 999:
        totnum += num
        contnum += 1
print(f'Você digitou {contnum} termos e a soma total deles equivale a {totnum}.')