# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo de média ponderada

print("Vamos calcular a nota média do aluno")

nota1 = float(input("Digite a primeira nota: "))

while ((nota1 < 0) | (nota1 > 10)):
    nota1 = float(input("Nota digitada é incorreta. Digite novamente a primeira nota: "))
    
nota2 = float(input("Digite a segunda nota: "))

while ((nota2 < 0) | (nota2 > 10)):
    nota2 = float(input("Nota digitada é incorreta. Digite novamente a segunda nota: "))
    
nota3 = float(input("Digite a terceira nota: "))

while ((nota3 < 0) | (nota3 > 10)):
    nota3 = float(input("Nota digitada é incorreta. Digite novamente a terceira nota: "))

mediaponderada = (((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10)

print("A média do aluno é:", mediaponderada)
