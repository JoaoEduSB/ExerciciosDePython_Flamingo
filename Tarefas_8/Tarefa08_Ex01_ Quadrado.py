# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#1) Apresentar os quadrados dos números inteiros de 15 a 200.

print("")

print("Vamos exibir o quadrado dos números inteiros de 15 a 200:")

confirmacao = input("Digite alguma tecla para iniciar: ")

for contadora in range (15, 201, 1):
    quadrado = contadora ** 2
    print(contadora, "² =", quadrado,)

print("")