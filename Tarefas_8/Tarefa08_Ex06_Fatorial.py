# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#6) Elaborar um programa que apresente como resultado o valor do fatorial dos valores ímpares situados na faixa numérica de 1 a 10.

import math

print("")

print("\nVamos apresentar o fatorial de cada número ímpar entre 1 e 10")

confirmacao = input("Digite alguma tecla para iniciar: ")

for contadora in range (1, 10, 1):

    if contadora % 2 != 0: 

        fatorial = math.factorial(contadora)
        
        print("O fatorial de", contadora, "é:", fatorial)

print("")