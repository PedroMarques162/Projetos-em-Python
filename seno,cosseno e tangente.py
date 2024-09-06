import math
num = float(input('Digite o valor de um ângulo qualquer:'))
seno = math.sin(math.radians(num))
print('O ângulo de {}, o seu seno é {:.2f}'.format(num, seno))

cosseno = math.cos(math.radians(num))
print('O ângulo de {}, o seu cosseno é {:.2f}'.format(num , cosseno))

tangente = math.tan(math.radians(num))
print('O ângulo de {}, a sua tangente é {:.2f}'.format(num, tangente))