# EXERCICIO 27. Vamos ver se o primeiro numero inserido é maior ou menor do que os outros.

num1 = input("Insira seu primeiro numero: ")
num2 = input("Insira seu segundo numero: ")
num3 = input("Insira seu terceiro e último numero: ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

print("\n______________________")
print("EXERCICIO 27")
print("￣￣￣￣￣￣￣￣￣￣￣￣")
print("\n::::::::::::::::::::::")
if num1 > num2 and num1 < num3:
    print(f"{num1} é maior que {num2}: VERDADEIRO e menor que {num3}: VERDADEIRO")    
elif num1 < num2 and num1 > num3:
    print(f"{num1} é maior que {num2}: FALSO e menor que {num3}: FALSO")
elif num1 < num2 and num1 < num3:
    print(f"{num1} é maior que {num2}: FALSO e menor que {num3}: VERDADEIRO") 
elif num1 > num2 and num1 > num3:
    print(f"{num1} é maior que {num2}: VERDADEIRO e menor que {num3}: FALSO") 
print(":::::::::::::::::::::::")