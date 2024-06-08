# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#8) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

print("")
print("\nVamos calcular o valor da compra de maças\n")
print("")

quantMacas = int(input("Quantas maças você deseja comprar?\n"
"Digite: "))

if (quantMacas < 12):
    precoMacas = 1.3
else:
    precoMacas = 1.0
    
precoCompra = (quantMacas * precoMacas)

print("\nValor da compra: R$", format(precoCompra, '.2f'))
print("")