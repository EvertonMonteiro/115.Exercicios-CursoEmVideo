import math
c = float(input('Digite o valor de um ângulo qualquer: '))
sen = math.sin(math.radians(c))
cos = math.cos(math.radians(c))
tan = math.tan(math.radians(c))
print(f'O Seno de {c}° equivale a: {sen:.2f}\nO Cosseno de {c}° equivale a: {cos:.2f}')
print(f'A Tangente de {c}° equivale a: {tan:.2f}')
