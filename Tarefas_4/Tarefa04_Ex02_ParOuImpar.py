# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar

#2) Faça um programa que peça ao usuário para digitar um número e informe se é par ou ímpar.

print("Vamos verificar se o número digitado é par ou ímpar")

numero = int(input("Digite o número: "))

if (numero % 2 == 0) :
    print("O número", numero,"é par")
else :
    print("O número", numero,"é ímpar")