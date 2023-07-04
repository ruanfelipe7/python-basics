######################## Dicionarios ##########################

##################### Criando Dicionarios #####################
dicionario1 = {"A": "AMEIXA", "B": "BOLA", "C": "CACHORRO"}

##################### Imprimindo o valor de uma determinada chave #####################
print(dicionario1["A"])

##################### Imprimindo o Dicionario #####################
print(dicionario1)

##################### Imprimindo Chave com Valor #####################
for chave in dicionario1:
	print(chave + " - " + dicionario1[chave])

##################### Imprimindo os itens do dicionario no formato de tupla #####################
for i in dicionario1.items():
	print(i)	

##################### Imprimindo os valores do Dicionario #####################
for i in dicionario1.values():
	print(i)

##################### Imprimindo as chaves Dicionario #####################
for i in dicionario1.keys():
	print(i)	