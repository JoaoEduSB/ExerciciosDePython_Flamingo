# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#8) Elaborar um programa que possibilite calcular a área total de uma residência (sala, cozinha, banheiro, quartos, área de serviço, quintal, garagem, etc.). O programa deve solicitar a entrada do nome, a largura e o comprimento de um determinado cômodo. Em seguida, deve apresentar a área do cômodo lido e também uma mensagem solicitando do usuário a confirmação de continuar calculando novos cômodos. Caso o usuário responda “NAO”, o programa deve apresentar o valor total acumulado da área residencial.

decisao = ""
totalArea = 0

print("\nEsse é um programa de cálculo de área dos cômodos de uma residência\n")

decisao = input("Você deseja calcular?\n"
      "Digite Sim ou Não: ")

print("")

while (decisao != "Não"):
    
    comodo = input("Digite o nome do cômodo: ")
    
    largura = float(input("Digite a largura do cômodo: "))

    comprimento = float(input("Digite o comprimento do cômodo: "))

    area = largura * comprimento    
    print(f"{comodo} tem {area}m².")
    
    decisao = input("\nDeseja continuar calculando a área de outros cômodos?"
               "\nDigite Sim ou Não: ")
    
    print("")

    totalArea += area
    
    if (decisao == "Não"):
        break
    
print("A área total dos cômodos calculados é: ", totalArea)

print("")