from math import sqrt,floor, ceil
num = int(input('digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('Arredonndando para baixo a raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
print('Arredonndando para cima a raiz de {} é igual a {:.2f}'.format(num, ceil(raiz)))
