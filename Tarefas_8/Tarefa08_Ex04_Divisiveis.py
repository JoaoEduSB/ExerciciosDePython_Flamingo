# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
#4) Apresentar todos os números divisíveis por 4 que sejam menores que 200. Para verificar se o número é divisível por 4, efetuar dentro da malha a verificação lógica desta condição com a instrução se, perguntando se o número é divisível; sendo, mostre-o; não sendo, passe para o próximo passo. A variável que controlará o contador deve ser iniciada com o valor 1.

print("")

print("\nVamos exibir os números divisiveis por 4 menores que 200")

confirmacao = input("Digite alguma tecla para iniciar: ")

print("")

print("Os números divisíveis por 4 são: ")
for contadora in range (1, 201, 1):
    if (contadora % 4 == 0):
        print(contadora)

print("")