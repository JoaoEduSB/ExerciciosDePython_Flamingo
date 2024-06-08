# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#13) Ler um valor e escrever se é positivo, negativo ou zero.

print("\nVamos validar se o número é positivo, negativo ou zero\n")

numero = int(input("Digite o valor: "))

if (numero == 0):
    print("O número é", numero)

elif (numero < 0):
    print("O número", numero, "é negativo.")
else:
    print("O número", numero, "é positivo.")
    
print("")