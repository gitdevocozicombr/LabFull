'''
Desafio 017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
retangulo, calcule e mostre o cumprimento da hipotenusa.
'''
import math
coposto = float(input('Digite o Cateto Oposto: '))
cadjacente = float(input('Digite o Cateto adjacente: '))
hipotenusa = math.hypot(coposto,cadjacente)
print(hipotenusa)
