# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#12) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'

print("\nVamos verificar o saldo do cliente e algumas informações dele\n")

conta = int(input("Digite a sua conta: "))
saldo = int(input("Digite o seu saldo: "))
debito = int(input("Digite o débito da sua conta: "))
credito = int(input("Digite o crédito da sua conta: "))

saldo_atual = (saldo - debito + credito)

if (saldo_atual >= 0):
    print("O seu saldo é positivo:", saldo_atual)
else:
    print("O seu saldo é negativo:", saldo_atual)

print("")