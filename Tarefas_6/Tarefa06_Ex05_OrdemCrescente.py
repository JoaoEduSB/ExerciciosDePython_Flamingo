# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# 5) Efetuar a leitura de três valores (variáveis A, B e C) e apresentá-los dispostos em ordem crescente.

print("Vamos ler 3 valores e exibi-los em ordem crescente")

valorA = int(input("Digite o primeiro valor: "))
valorB = int(input("Digite o segundo valor: "))
valorC = int(input("Digite o terceiro valor: "))

valores = [valorA, valorB, valorC]

valores.sort()

print("\nOs valores em ordem crescente são:", valores[0], ",", valores[1], ",", valores[2])

print("")