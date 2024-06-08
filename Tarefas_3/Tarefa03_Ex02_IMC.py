# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo do IMC

#2) Crie um programa que solicite ao usuário sua altura e peso, e calcule seu índice de massa corporal (IMC).

print("Vamos ler os seus dados e calcular o seu imc")

altura = float(input("Digite a sua altura em: "))
peso = float(input("Digite o seu peso em kg: "))

imc = (peso / (altura * altura))

if (imc < 16):
      print("Seu IMC é igual a magreza grave")
elif (imc < 16.9):
      print("Seu IMC é igual a magreza moderada")
elif (imc < 18.5):
      print("Seu IMC é igual a magreza leve")
elif (imc < 24.9):
      print("Seu IMC é igual peso ideal")
elif (imc < 29.9):
      print("Seu IMC é igual sobrepeso")
elif (imc < 34.9):
      print("Seu IMC é igual a obesidade grau I")
elif (imc < 40):
      print("Seu IMC é igual a obesidade grau II ou severa")
else:
      print("Seu IMC é igual III ou mórbida")
