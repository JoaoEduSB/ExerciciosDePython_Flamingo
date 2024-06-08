# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo da área de um hexágono

#14) Escreva um algoritmo para ler as dimensões de um hexagono, calcular e escrever a área do hexagono.

import math

print("Vamos ler o lado do hexágono e exibir a sua área em m²")

lado = float(input("Digite o valor de um dos lados do retângulo em m²: "))

area = ((3 * pow(lado, 2) * math.sqrt(3)) / 2) 

print("A área do hexágono é:", round(area,2),"m²")