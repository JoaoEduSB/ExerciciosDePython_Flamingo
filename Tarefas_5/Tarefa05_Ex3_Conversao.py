# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

#3) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):

# print ("\nVamos ler as notas do aluno e dizer se ele foi aprovado ou não\n")

# nota1 = float(input("Digite a sua primeira nota: "))

# while (nota1 < 0) | (nota1 > 10):
#     nota1 = float(input("A nota digitada é invalida.\n"
# "Digite novamente a sua primeira nota: "))


# nota2 = float(input("Digite a sua segunda nota: "))
# while (nota2 < 0) | (nota2 > 10):
#     nota2 = float(input("A nota digitada é invalida.\n"
# "Digite novamente a sua segunda nota: "))

# media = ((nota1 + nota2) / 2)

# if (media >= 6):
#     print("O aluno foi aprovado com média:", media)
# else:
#     print("O aluno foi reprovado com média:", media)
    
print("Vamos calcular a nota média do aluno")

nota1 = float(input("Digite a primeira nota: "))

while ((nota1 < 0) | (nota1 > 10)):
    nota1 = float(input("Nota digitada é incorrta. Digite novamente a primeira nota: "))
    
nota2 = float(input("Digite a segunda nota: "))

while ((nota2 < 0) | (nota2 > 10)):
    nota2 = float(input("Nota digitada é incorrta. Digite novamente a segunda nota: "))
    
nota3 = float(input("Digite a terceira nota: "))

while ((nota3 < 0) | (nota3 > 10)):
    nota3 = float(input("Nota digitada é incorreta. Digite novamente a terceira nota: "))

mediaponderada = (((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10)

print("A média do aluno é:", mediaponderada)