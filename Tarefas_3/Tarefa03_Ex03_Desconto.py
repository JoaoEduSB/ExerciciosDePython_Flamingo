# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo de desconto

#3) Faça um programa que pergunte ao usuário o valor do produto e o percentual de desconto, e retorne o valor final após o desconto.

print("\nVamos calcular o valor de desconto de sua compra")

valorProd = float(input("Digite o valor do produto: R$"))

print("\nVocê terá que digitar o valor como inteiro, exemplo: caso seja 10%, digite apenas 10")

percentual = float(input("Digite o percentual de desconto: R$"))

percentualCalculado = (percentual / 100)

valorAtualizado = (valorProd * percentualCalculado)

desconto = (valorProd - valorAtualizado)


print("\n O valor normal do produto é: R$", valorProd, "\n",
      "O valor do produto com desconto é: R$", desconto, "\n",
      "O desconto foi de: R$", valorAtualizado,"\n")
