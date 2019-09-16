#Desafio 011
#Desenvolva um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
#a quantidade de tinta nevessária para pinta-la, sabendo que cada litro de tinta pinta uma área de
#2m²
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
tinta  = (largura * altura) / 2
print(tinta)