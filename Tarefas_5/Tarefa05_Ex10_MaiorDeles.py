# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#10) Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

print("\nVamos escrever o maior valor lido\n")

valorA = int(input("Digite o primeiro valor: "))
valorB = int(input("Digite o segundo valor: "))

if (valorA > valorB):
    maiorDeles = valorA
else:
    maiorDeles = valorB

print("\nO maior valor digitado foi:", maiorDeles)
print("")