import math
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))
print('Arredonndando para baixo a raiz de {} é igual a {:.2f}'.format(num, math.floor(raiz)))
print('Arredonndando para cima a raiz de {} é igual a {:.2f}'.format(num, math.ceil(raiz)))
'''
#Importanto apenas duas funcionalidades da lib math
from math import math sqrt,floor
'''