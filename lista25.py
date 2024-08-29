print('\n')
#QUESTÃO 25 - 
print("--------------------")
#Primeiramente, Pedimos ao usuário colocar dados variáveis numéricos
C = int(input("Digite o valor do capital: "))
i = int(input("Insira seu numero em porcentagem: "))
t = int(input("Digite o seu tempo em anos: "))
print("--------------------")
#Depois fazemos um cálculo para descobrir o valor de Juros simples
J = C * i / 100 * t
print("--------------------")
#Para finalizar, exibimos o resultado do cálculo que fizemos
print(f"O resultado final do cálculo para Juros é igual a: {J}")
print("--------------------")
