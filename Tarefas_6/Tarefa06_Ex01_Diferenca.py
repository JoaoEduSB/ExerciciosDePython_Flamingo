# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#1) Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor.

print("\nVamos ler 2 valores e apresentar a diferença entre o menor para o maior\n")

valorA = int(input("Digite o primeiro valor: "))
valorB = int(input("Digite o segundo valor: "))

if (valorA > valorB):
    resultado = valorA - valorB
else:
    resultado = valorB - valorA

print("O resultado da diferença dos dois é :", resultado)

print("")