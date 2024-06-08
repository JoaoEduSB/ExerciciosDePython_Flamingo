# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo da área de um círculo

#13) Escreva um algoritmo para ler as dimensões de um circulo (raio), calcular e escrever a área do circulo. a=pi*r²

print("Vamos ler as dimensões do círculo e exibir a sua área em m²")

diametro = float(input("Digite o diametro do círculo em m²: "))

raio = (diametro / 2)
area = 3.14 * (raio ** 2)

print("A área do círculo é:", area,"m²")