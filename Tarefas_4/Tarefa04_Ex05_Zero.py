# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

#5) Escreva um programa que peça ao usuário para digitar um número e verifique se é positivo, negativo ou zero.

print("Vamos digitar um número e validar se ele é positivo, negativo ou zero")

numero = int(input("Digite o número: "))

if (numero == 0):
    print("O número", numero, "é 0")
elif (numero < 0):
    print("O número", numero,"é menor que 0")
else :
    print ("O número", numero, "é maior que 0")