# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#5) Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, de 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. O programa deve apresentar os valores das duas temperaturas. A fórmula de conversão é F = 9C+160/5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

contadora = 10

print("")

print("\nVamos mostrar a conversão de graus Celsius para Fahrenheit")

confirmacao = input("Digite alguma tecla para iniciar: ")

while (contadora <= 100):

    fahrenheit = (9 * contadora + 160) / 5
        
    print("A temperatura de", contadora,"C° convertida será:", fahrenheit, "°F")

    contadora += 10

print("")