# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#4) Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20. Para verificar se o número é ímpar, efetuar dentro da malha a verificação lógica desta condição com a instrução se, perguntando se o número é ímpar; sendo, mostre-o; não sendo, passe para o próximo passo

contadora = 0

print("")

print("\nVamos exibir os números ímpares entre 0 e 20")

confirmacao = input("Digite alguma tecla para iniciar: ")

while (contadora <= 20):

    if (contadora % 2 != 0):
        
        print(contadora)

    contadora += 1

print("")