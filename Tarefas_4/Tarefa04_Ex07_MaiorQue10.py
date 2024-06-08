# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de contagem de vogais de uma frase

#7) Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!

print("\nVamos verificar se o número digitado é maior que 10\n")

numero = int(input("Digite um número: "))

if (numero == 10):
    print("\nO número", numero,"é igual a 10.\n")

elif (numero > 10):
    print("\nO número", numero,"é maior que 10.\n")
    
else:
    print("\nO número", numero,"é menor que 10.\n")