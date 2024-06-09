# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#2) Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número lido como sendo um valor positivo, ou seja, o programa deverá apresentar o módulo de um número fornecido. Lembre-se de verificar se o número fornecido é menor que zero; sendo, multiplique-o por -1.

print("")

print("Vamos ler um número e apresentar o seu módulo''")
print("")

numero = int(input("Digite um número: "))

if (numero < 0):
	modulo = numero * -1
	print("O módulo do número", numero, "é:", modulo)
	
else:
	modulo = numero
	print("O módulo do número", numero, "é:", modulo)
    
print("")