# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

# 9) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

print("\nVamos calcular o valor da compra de maças\n")

quantMacas = int(input("Quantas maças você deseja comprar?\n"
"Digite: "))

if (quantMacas < 12):
    precoMacas = 1.3
else:
    precoMacas = 1.0
    
precoCompra = (quantMacas * precoMacas)

print("\nValor da compra: R$", format(precoCompra, '.2f'))