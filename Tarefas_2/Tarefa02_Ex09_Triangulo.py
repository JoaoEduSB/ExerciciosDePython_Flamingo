# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo da área de um triângulo

#9) Escreva um algoritmo para ler as dimensões de um triângulo (base e altura), calcular e escrever a área do triângulo. Dica a=b.h/2

print("Vamos ler as dimensões do triângulo e exibir a sua área em m²")

base = float(input("Digite a base do triângulo em m²: "))
altura = float(input("Digite a altura do triângulo em m²: "))

area = (base * altura) / 2

print("A área do triângulo é:", area,"m²")