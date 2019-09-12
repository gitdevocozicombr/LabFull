'''
Desafio 18:
Desenvolva um programa que leia um angulo qualquer e mostre na tela o valor do seno,
cosseno e tangente deste angulo.
'''
import math
angulo = float(input('Digite o valor de um angulo: '))
seno = format(math.sin(angulo))
print(seno)