# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#9) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

print("\nVamos verificar se uma pessoa pode votar\n")

anoNascimento = int(input("Digite o seu ano de nascimento: "))

anoAtual = int(input("Digite o ano atual: "))

idade = anoAtual - anoNascimento

print("A idade da pessoa é:", idade)
print("")