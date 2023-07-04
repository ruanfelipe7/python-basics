# -*- coding: utf-8 -*-
print("Olá Mundo!")
#Comentario do codigo

print("-------------------Operações Matemáticas-----------------------")
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(3 / 2)
print(2 ** 3)  #Exponenciação
print(10 % 3)  #Modulo


print("--------------------Variaveis-----------------------")

variavel = "Mensagem na variavel"
print(variavel)
print(variavel)
print(variavel)

var1 = 1    #variavel inteira
var2 = 1.1  #variavel float
var3 = "String"  #variavel string
var4 = True    #variavel booleana

print(var1, var2, var3, var4)


print("--------------------Operadores lógicos-----------------------")
x = 2
y = 3
print(x == y)
print(x < y)
print(x > y)


print("--------------------Operadores relacionais-----------------------")
print(x == y or x < y)
print(x < y and x == y)

print("--------------------If, else, elif-----------------------")
if(x < y):
	print("x é menor que y")
elif(x == y):
	print("x é igual a y")
else:
	print("x é maior que y")		


print("-------------------While------------------------")
x = 1
while(x < 10):
	print(x)
	x += 1

print("-------------------For------------------------")

lista = [1,2,3,4,5]
lista2 = ["ola", "mundo", "!"]
lista3 = [0, "teste", 2.3, True]

for i in lista:
	print(i)
for i in lista3: 
	print(i)	

print("-------------------For e Range------------------------")

for i in range(10):
	print(i)

for i in range(5, 20):
	print(i)

for i in range(10, 20, 2):
	print(i)


print("-------------------Strings------------------------")

print("--------------------Concatenação-----------------------")
var1 = "Ruan"
var2 = "Felipe"
concat = var1 + " " + var2
print(concat)

print("--------------------Tamanho de uma string-----------------------")
tam = len(concat)
print(tam)

print("--------------------Navegação pelo indice-----------------------")
letra = concat[5]
print(letra)

print("--------------------Parte de uma string-----------------------")
substring = concat[7:11]
print(substring)
substring2 = concat[5:]
print(substring2)

print("--------------------Caixa de uma string-----------------------")
minusculo = concat.lower()
print(minusculo)
maiusculo = concat.upper()
print(maiusculo)

print("--------------------Remover espaço e caracteres especiais no começo e fim da string-----------------------")
nome = "   Ruan Felipe        \n \n  "
print(nome.strip())

print("--------------------Quebrando a string-----------------------")
seq = "O rato roeu a roupa do rei de roma"
lista1 = seq.split(" ")
print(lista1)
lista2 = seq.split("r")
print(lista2)

print("--------------------Buscando substring-----------------------")
busca = seq.find("rei")
print(busca)
print(seq[busca:])


print("--------------------Substituir parte de uma string-----------------------")
nova_seq = seq.replace("o rei", "a rainha")
print(nova_seq)


print("--------------------Funções-----------------------")

def soma(num1, num2):
	return (num1 + num2)

def multiplicacao(num1, num2):
	return (num1 * num2)

s = soma(10, 10)	
print(s)
m = multiplicacao(10, 10)
print(m)

print("--------------------Arquivos-----------------------")
arquivo = open("arquivo.txt", "r")
#linhas = arquivo.readlines()
#print(linhas)

texto_completo = arquivo.read()
print(texto_completo)	
arquivo.close()

w = open("arquivo2.txt", "w")
w.write("Esse é um novo arquivo 2\n")
w.close()	

a = open("arquivo2.txt", "a")
a.write("Esse é o novo arquivo 2\n")
a.close()