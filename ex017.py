import math
cat1 = float(input('Digite o valor do cateto oposto: '))
cat2 = float(input('Digite o valor do cateto adjascente: '))
hipotenusa = math.hypot(cat1, cat2)
print (f'A hipotenusa do cateto oposto {cat1} e do cateto adjascente {cat2} equivale a {hipotenusa:.2f}.')