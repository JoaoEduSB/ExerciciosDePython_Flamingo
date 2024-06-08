# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo de nota média

#4) Faça um programa que receba três notas de um aluno e calcule sua média.

print("\nVamos calcular a nota média do aluno\n")

nota1 = int(input("Digite a sua primeira nota: "))
nota2 = int(input("Digite a sua segunda nota: "))
nota3 = int(input("Digite a sua terceira nota: "))

media = ((nota1 + nota2 + nota3) / 3)

print("\nA nota média do aluno é: ", round(media, 1))
