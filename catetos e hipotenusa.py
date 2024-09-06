import math
from math import hypot
co = float(input('Digite o caceto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

'''co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
