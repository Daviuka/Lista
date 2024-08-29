
# Exercício 18. Este exercício tem o propósito de exibir o dobro, triplo, e a raiz de um número
# inserido.

import math

num = input("Insira seu numero: ")
num = int(num)
num_conc = (u"\u221a") + str(num)

# Nossos cálculos vão aqui:
dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)
raiz = float(raiz)

# Vamos imprimir os resultados:
print("\n______________________")
print("EXERCICIO 18")
print("￣￣￣￣￣￣￣￣￣￣￣￣")
print("\n::::::::::::::::::::::")
print(f"Você inseriu: {num}")
print(f"O dobro será: {dobro}")
print(f"O triplo será: {triplo}")
print(u"O resultado de" , num_conc , f"será: {raiz:.2f}")
print("::::::::::::::::::::::")