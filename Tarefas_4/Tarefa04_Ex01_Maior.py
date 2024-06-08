# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação de idade

#1) Faça um programa que receba a idade do usuário e imprima se ele é maior de idade ou não.

print("Vamos verificar se você é maior de idade ou não")

idade = int(input("Digite a sua idade: "))

if (idade < 18) :
    print("Você tem", idade, "anos, portanto é menor de idade")
else :
    print("Você tem", idade, "anos, portanto é maior de idade")