# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#3) Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

contadora = 0
resultado = 0

print("")

print("\nVamos exibir a soma dos números pares de 1 a 500")

confirmacao = input("Digite alguma tecla para iniciar: ")

while (contadora < 501):

    if (contadora % 2 == 0):
        resultado += contadora

    contadora += 1

print(resultado)

print("")