# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#4) Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 7. Se o valor da média for menor que 7, solicitar a nota de exame, somar com o valor da média e obter nova média. Se a nova média for maior ou igual a 5, apresentar uma mensagem dizendo que o aluno foi aprovado em exame. Se o aluno não foi aprovado, indicar uma mensagem informando esta condição. Apresentar com as mensagens o valor da média do aluno, para qualquer condição.

mediaExame = 0
aprovado = "aprovado"

print("")
print("Vamos ler 4 notas e verificar se o aluno foi aprovado")
print("")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("")
if media >= 7:
    print("O aluno foi aprovado com média:", round(media, 1))
    aprovado = "aprovado"
else:
    mediaExame = float(input("O aluno não passou com as notas avaliadas.\nDigite a sua nota de exame: "))
    mediaExame = (media + mediaExame) / 2
    aprovado = "reprovado"
    if aprovado == "aprovado":
        print("")
    elif mediaExame >= 5:
        print("O aluno foi aprovado com a nota de exame.\nSua média foi: ", round(mediaExame, 1))
    else:
        print("O aluno foi reprovado com média:", round(mediaExame))
        
print("")