# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

#3) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):

#C= (F - 32)*5/9

#Observação: Para testar se a sua resposta está correta saiba que 100oC = 212F

print("\nVamos converter uma temperatura de Fahrenheit para celsius\n")

fahrenheit = float(input("Digite a temperatura em fahrenheit: "))

celsius = ((fahrenheit - 32 ) * 5) / 9

<<<<<<< HEAD:Tarefas_5/Tarefa05_Ex3_Conversao.py
print("A conversão de", fahrenheit, "°F, resulta em", celsius, "°C.\n")
=======
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
>>>>>>> 9b02efa1e6af1b62cc1452ce94d27de56ea5262e:Tarefas_5/Tarefa05_Ex03_Conversao.py
