# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo da área de um trapézio

#12) Escreva um algoritmo para ler as dimensões de um trapézio (base amior, base menor e altura), calcular e escrever a área do trapézio. a=(B+b).h/2

print("Vamos ler as dimensões do trapézio e exibir a sua área em m²\n")

baseSup = float(input("Digite a base superior do trapézio em m²: "))
baseInf = float(input("Digite a base inferior do trapézio em m²: "))
altura = float(input("Digite a altura do trapézio em m²: "))

area = (((baseSup + baseInf) * altura) / 2)

print("A área do trapézio é:", area,"m²")