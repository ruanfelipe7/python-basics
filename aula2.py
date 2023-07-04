# -*- coding: utf-8 -*-
####################  Criando listas ########################
minha_lista = ["abacaxi", "malancia", "abacate", "manga"]
minha_lista_2 = [1, 2, 3, 4, 5]
minha_lista_3 = ["abacaxi", 2, 8.5, True]
minha_lista_4 = []

####################  Imprimindo listas ########################
print(minha_lista)
print(minha_lista_2)
print(minha_lista_3)

####################  Imprimindo um item da lista ########################
print(minha_lista[2])

####################  Imprimindo cada item da lista ########################
for item in minha_lista:
	print(item)

####################  Tamanho da lista ########################
tamanho = len(minha_lista)
print("Tamanho: ", tamanho)

####################  Adicionando elementos na lista ########################
minha_lista.append("limao")	
print(minha_lista)
minha_lista_4.append(57)
print(minha_lista_4)

#################### Verificando se um elemnto está na lista ########################
if 3 in minha_lista_2:
	print("3 esta na lista")

####################  Deletando os itens da lista ########################
del minha_lista[2:]	
print(minha_lista)

####################  Deletando toda a lista ########################
del minha_lista[:]
print(minha_lista)

###################  Listas ###########################
lista = [124, 345, 5, 72, 46, 6, 7, 1, 3, 7, 0]
lista2 = [124, 345, 5, 72, 46, 6, 7, 1, 3, 7, 0]

################## Ordenando uma lista numerica ######################
lista_ordenada = sorted(lista)
lista.sort()
print(lista)
print(lista_ordenada)

################## Invertendo uma lista ######################
lista2.reverse()
print(lista2)

################## Ordenando uma lista numerica de modo decrescente ######################
lista2.sort(reverse=True)
print(lista2)

################## Ordenando uma lista de strings ######################
lista3 = ["bola", "abacate", "dinheiro"]
lista3.sort()
print(lista3)