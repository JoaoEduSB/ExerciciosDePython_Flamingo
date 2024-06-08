# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

#6) Faça um programa que receba um número inteiro e retorne se é primo ou não.

print("Vamos verificar se um número é primo")

numero = int(input("Digite um número inteiro: "))

numero_primo = True

if (numero <= 1):
    numero_primo = False
    
elif (numero == 2):
    numero_primo = True
    
elif (numero % 2 == 0):
    numero_primo = False
    
else:
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            numero_primo = False
            break

if numero_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")