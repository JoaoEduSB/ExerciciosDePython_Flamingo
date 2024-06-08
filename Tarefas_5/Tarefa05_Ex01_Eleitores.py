# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de cálculo de eleitores

#Calcular e escrever o percentual de eleitores

print("Vamos ler o número de eleitores e escrever o percentual de cada um em relação ao total")

votosBrancos = int(input("Digite o total de votos Brancos: "))
votosNulos = int(input("Digite o total de votos Nulos: "))
votosValidos = int(input("Digite o total de votos Válidos: "))

totalVotos = votosBrancos + votosNulos + votosValidos

percBrancos = (votosBrancos * 100) / totalVotos
percNulos = (votosNulos * 100) / totalVotos
percValidos = (votosValidos * 100) / totalVotos

print("Total de votos dos eleitores:", totalVotos)
print("Percentual de votos brancos: ", percBrancos)
print("Percentual de votos brancos: ", percNulos)
print("Percentual de votos brancos: ", percValidos)