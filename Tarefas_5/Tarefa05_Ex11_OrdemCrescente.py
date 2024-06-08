# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#11) Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

print("\nVamos escrever os valores lidos em ordem crescente\n")

valorA = int(input("Digite o primeiro valor: "))
valorB = int(input("Digite o segundo valor: "))

if (valorA > valorB):
    maiorDeles = valorA
    menorDeles = valorB
else:
    maiorDeles = valorB
    menorDeles = valorA

print("\nOs valores em ordem crescente são:", menorDeles, ",", maiorDeles)
print("")