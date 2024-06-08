# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

#4) Escreva um programa que peça ao usuário para digitar três números e retorne o maior deles.

print("Vamos digitar 3 números e exibir o maior deles")

numero1 = int(input("Digite o primeiro número: "))

maiordeles = numero1

numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if (maiordeles < numero2):
    maiordeles = numero2
if (maiordeles < numero3):
    maiordeles = numero3

print("O maior número digitado foi:", maiordeles)