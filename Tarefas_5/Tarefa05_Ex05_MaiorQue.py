# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação

print("Vamos validar se o valor digitado é maior ou menor que 10")

valor = int(input("Digite o valor: "))

if (valor == 10):
    print("O valor", valor, "é igual a 10.")
elif (valor > 10):
    print("O valor", valor ,"é maior que 10")
else:
    print("O valor", valor, "é menor que 10")