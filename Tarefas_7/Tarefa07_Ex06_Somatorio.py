# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#6) Elaborar um programa que efetue a leitura de 10 valores numéricos e apresente no final o total do somatório e a média aritmética dos valores lidos.

contadora = 1
soma = 0

print("")

print("\nVamos ler 10 valores e efetuar soma deles, e também exibir a média")

while (contadora < 11):

    valor = int(input(f"Digite o {contadora} ° valor: "))
    
    soma += valor
    
    contadora += 1


media = soma / 10

print("A soma dos valores digitados é:", soma, "\n"
        "A média dos valores é:", media, "\n")

print("")