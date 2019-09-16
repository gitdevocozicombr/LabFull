'''
Desafio 016
Desenvolva um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua
porção inteira.
Ex.: Existe um numero: 6.127, o numero seria 6.
'''
import math
numero = float(input('Digite um numero: '))
print('O numero arredondado é {}'.format(math.floor(numero)))