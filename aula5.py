########### list comprehension ###############

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
z = [i for i in x if (i % 2)==1]

print(x)
print(y)
print(z)

########### Enumerate ###############
lista = ["abacate", "bola", "cachorro"]

for i, nome in enumerate(lista):
	print(i, nome)

################# Filter ####################	
def pares(j):
	if ((j % 2) == 0):
		return j
	
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = filter(pares, lista2)
print(list(lista_pares))


################### Map #######################

def dobro(x):
	return x * 2

valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valor_dobrado = map(dobro, valor)
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)


################### Zip ###########################
lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$ 2,00", "R$ 5,00", "Nao tem preco", "Nao tem preco", "Nao tem preco"]

for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor)
