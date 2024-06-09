# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#7) Elaborar um programa que apresente os resultados da soma e da média aritmética dos valores pares situados na faixa numérica de 50 a 70.

contadora = 49
soma = 0
pares = 0

print("")

print("\nVamos exibir a soma e a média dos valores pares entre 50 e 70")

confirmacao = input("Digite alguma tecla para iniciar: ")

while (contadora <= 70):
    
    if (contadora % 2 == 0):

        soma += contadora

        pares += 1 

    contadora += 1
        

media = soma / pares

print("A soma dos valores digitados é:", soma, "\n"
        "A média dos valores é:", media, "\n")

print("")