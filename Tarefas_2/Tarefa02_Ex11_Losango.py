# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo da área de um losango

#11) Escreva um algoritmo para ler as dimensões de um losango (diagonal maior, diagonal menor), calcular e escrever a área do losango. Dica a=D.d/2

print("Vamos ler a maior e a menor dimensão do losango e exibir a sua área em m²")

dimensaoMaior = float(input("Digite a maior dimensão do losango em m²: "))
dimensaoMenor = float(input("Digite a menor dimensão do losango em m²: "))

area = dimensaoMaior * dimensaoMenor / 2

print("A área do losango é:", area,"m²")