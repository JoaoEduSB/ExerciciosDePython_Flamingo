# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#14) Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

print("\nVamos escrever o maior valor lido\n")

valorA = int(input("Digite o primeiro valor: "))
valorB = int(input("Digite o segundo valor: "))
valorC = int(input("Digite o terceiro valor: "))

if (valorA > valorB) & (valorA > valorC):
    maiorDeles = valorA
elif (valorB > valorA) & (valorB > valorC):
    maiorDeles = valorB
else:
    maiorDeles = valorC

print("O maior valor é:", maiorDeles)
