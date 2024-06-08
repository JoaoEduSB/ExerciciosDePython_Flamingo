# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo de salário

#2) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

print("Vamos calcular o reajuste do salário de um funcionário")

salarioAtual = float(input("Digite o salário atual do funcionário: "))

reajuste = float(input("Digite o reajuste como valor inteiro\n"
                       "Exemplo: caso seja 10 porcento de reajuste, digite apenas 10\n"
                       "Digite o reajuste: "))

salarioNovo = (salarioAtual * (reajuste / 100) + salarioAtual)

print("O salário do funcionário reajustado é: R$", salarioNovo)