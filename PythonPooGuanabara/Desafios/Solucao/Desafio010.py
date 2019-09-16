# Desafio 010
# Desenvolva um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# Dolares ela pode comprar.
# 1 Dollar = 3,27
dinheiro = float(input('Quanto você tem na carteira: R$'))
dolar = float(3.75)
convercao = dinheiro / dolar
print('O Valor em dolar equivale a {}'.format(convercao) )