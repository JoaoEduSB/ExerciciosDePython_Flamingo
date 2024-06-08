# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

#3) Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) ela possui.

print("Vamos verificar quantas vogais a frase digitada possui")

frase = str(input("Digite a frase: "))
caracteres = ['a', 'e', 'i', 'o', 'u']

ocorrencias = [frase.count(c) for c in caracteres]

for caractere, contagem in zip (caracteres, ocorrencias):
    print(f"A vogal '{caractere}' aparece '{contagem}' vezes na frase.")