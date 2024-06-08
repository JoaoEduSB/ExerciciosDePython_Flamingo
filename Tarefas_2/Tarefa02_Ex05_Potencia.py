# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo de potência

#5) Escreva um algoritmo para ler dois valores do teclado (base e exponenciação) e exibir como resposta a exponenciação.

print("Vamos calcular e exibir o resultado de uma potência")

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

potencia = base ** expoente

potencia2 = pow(base, expoente)

print("O resultado da potência de", base, "Elevado a", expoente, "é:", potencia)
print("O resultado da potência de", base, "Elevado a", expoente, "é:", potencia2)