# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#2_C) Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).

contadora = 0
resultado = 0

print("")

print("\nVamos exibir a soma dos 100 primeiros números inteiros")

confirmacao = input("Digite alguma tecla para iniciar: ")

for contadora in range (1, 101, 1):

    resultado += contadora

    print(contadora, resultado)

print("")