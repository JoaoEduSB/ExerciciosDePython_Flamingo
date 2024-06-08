# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

#10) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

print ("\nVamos ler as notas do aluno e dizer se ele foi aprovado ou não\n")

nota1 = float(input("Digite a sua primeira nota: "))

while (nota1 < 0) | (nota1 > 10):
    nota1 = float(input("A nota digitada é invalida.\n"
"Digite novamente a sua primeira nota: "))


nota2 = float(input("Digite a sua segunda nota: "))
while (nota2 < 0) | (nota2 > 10):
    nota2 = float(input("A nota digitada é invalida.\n"
"Digite novamente a sua segunda nota: "))

media = ((nota1 + nota2) / 2)

if (media >= 6):
    print("O aluno foi aprovado com média:", media)
else:
    print("O aluno foi reprovado com média:", media)