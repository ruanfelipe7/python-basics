# -*- coding: utf-8 -*-

########################  Numeros Aleatorios ###########################

import random

numero = random.randint(0, 10)
print(numero)

lista = [6, 45, 9]
numero2 = random.choice(lista)
print(numero2)


######################### Exceções ############################
a = 2
b = 0

try:
	print(a/b)
except:
	print("Não é perimitida divisão por zero")	

print(a/a)	