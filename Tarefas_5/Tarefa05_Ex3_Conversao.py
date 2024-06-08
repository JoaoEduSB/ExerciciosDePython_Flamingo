# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

#3) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):

#C= (F - 32)*5/9

#Observação: Para testar se a sua resposta está correta saiba que 100oC = 212F

print("\nVamos converter uma temperatura de Fahrenheit para celsius\n")

fahrenheit = float(input("Digite a temperatura em fahrenheit: "))

celsius = ((fahrenheit - 32 ) * 5) / 9

print("A conversão de", fahrenheit, "°F, resulta em", celsius, "°C.\n")