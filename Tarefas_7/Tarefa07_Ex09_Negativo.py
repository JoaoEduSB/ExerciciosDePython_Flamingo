# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#9) Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser apresentados o maior e o menor valores informados pelo usuário.

print("\nVamos ler valores positivos e finalizar quando for inserido um valor negativo\n")

numero = int(input("Digite um número: "))

maiorNumero = numero
menorNumero = numero

while (numero >= 0):
    print("")

    numero = int(input("Digite um número: "))

    if (numero > maiorNumero):
        maiorNumero = numero
    
    if (numero < menorNumero):
        menorNumero = numero

print("\nO menor número digitado foi:", menorNumero, "\n"
      "O maior número digitado foi:", maiorNumero)

print("")