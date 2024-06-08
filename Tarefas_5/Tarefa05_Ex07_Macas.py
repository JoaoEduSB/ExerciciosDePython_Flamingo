# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#7) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra

print("")
print("Vamos calcular a compra de maças")
print("")


quantMacas = int(input("Digite a quantidade de maças que você deseja? : "))

if (quantMacas < 12) :
    preco = quantMacas * 1.30

else :
    preco = quantMacas * 1

total_compra = preco

print("O valor da compra da pessoa foi: R$" , round(total_compra, 2))
print("")