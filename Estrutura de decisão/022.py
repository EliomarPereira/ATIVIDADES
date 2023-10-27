#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

numero = float(input("Informe um número: "))

nu = numero % 2

if nu == 0:
    print("Esse número é um número par")
else:
    print("Esse número é um número impar")
