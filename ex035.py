print('Vamos analisar triângulos, digite os segmentos de reta a seguir')
t1 = float(input('Digite o primeiro segmento: '))
t2 = float(input('Digite o segundo segmento: '))
t3 = float(input('Digite o terceiro segmento: '))
if t1+t2>t3 and t2+t3>t1 and t1+t3>t2:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos não podem formar um triângulo!')
