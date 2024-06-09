# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#2) Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer

contadora = int(1)

print("")

print("\nVamos exibir a tabuada desejada")

numero = int(input("Digite o número da tabuada desejada: "))

print("")

print("Tabuada do", numero, ":")

for contadora in range (0, 11, 1):

    resultado = numero * contadora  

    print( numero, "x", contadora, "=", resultado)
    
print("")