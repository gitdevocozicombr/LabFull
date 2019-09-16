'''
Desafio 19:
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que qjude ele,
lendo o nome deles e escrevendo o nome do escolhido.
bibliografia:
https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
'''

import random
alunos = ['mateus', 'marcos', 'lucas', 'joão']
print(random.choice(alunos))


