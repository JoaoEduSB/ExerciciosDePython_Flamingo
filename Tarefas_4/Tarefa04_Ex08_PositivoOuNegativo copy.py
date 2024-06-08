# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

#8) Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo).

print("Vamos digitar um número e validar se ele é positivo ou negativo")

numero = int(input("Digite o número: "))

if (numero >= 0):
    print("O número", numero, "é positivo.")
else :
    print ("O número", numero, "é negativo.")