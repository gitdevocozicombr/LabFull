#Desafio 012
#Desenvolva um programa que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
preco = float(input('Digite o Preco do produto: '))
desconto = preco - (preco * 0.05)
print(desconto)