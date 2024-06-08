# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo de segundos

#5)Crie um programa que pergunte ao usuário a quantidade de dias, horas, minutos e segundos, e calcule o total em segundos.

print("\nVamos calcular a quantidade de segundos\n")

dias = int(input("Digite quantos dias você deseja calcular: "))
horas = int(input("Digite quantas horas você deseja calcular: "))
minutos = int(input("Digite quantos minutos você deseja calcular: "))
segundos = int(input("Digite quantos segundos você deseja calcular: "))

totalDias = (dias * 24) #Nessa linha estou convertendo os dias para horas, total dias recebe horas
totalHoras = ((horas + totalDias) * 60)
totalMinutos = ((totalHoras + minutos) * 60)
totalSegundos = (totalMinutos + segundos)
