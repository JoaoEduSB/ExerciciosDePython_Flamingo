# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#6) Elaborar um programa que efetue a leitura do nome e do sexo de uma pessoa, apresentando com saída uma das seguintes mensagens: "Ilmo Sr.", se o sexo informado como masculino, ou a mensagem "Ilma Sra.", para o sexo informado como feminino. Apresente também junto da mensagem de saudação o nome previamente informado.

print("")

print("\nVamos verificar o sexo da pessoa e informar uma saudação")

nome = input("Digite o seu nome: ")

sexo = input("Digite o seu sexo (M) para masculino e (F) para feminino: ")

if sexo == "M":
    print("Olá ilmo Sr.", nome, "seja bem-vindo.")

else:
    print("Olá ilma Sra.", nome, "seja bem-vinda.")
    
print("")