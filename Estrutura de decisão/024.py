#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite um número: "))


adicao = "1"
subtracao = "2"
divisao = "3"
multiplicacao = "4"

operacao = (input("Selecione a operação que deseja realizar: "))


if operacao == "1":
    adicao = num_1 + num_2
    adi = adicao % 2
    ad = adicao % 1
    
    if adi == 0:
        print("Número par")
    elif adi != 0:
        print("Número Impar")
    
    if adicao >= 0:
        print("Número Positivo")
    elif adicao < 0:
        print("Número Negativo")

    if ad == 0:
        print("É um número inteiro")
    elif ad != 0:
        print("É um número decimal")

if operacao == "2":
    subtracao = num_1 - num_2
    sub = subtracao % 2
    su = subtracao % 1
    
    if sub == 0:
        print("Número par")
    elif sub != 0:
        print("Número Impar")
    
    if subtracao >= 0:
        print("Número Positivo")
    elif subtracao < 0:
        print("Número Negativo")

    if su == 0:
        print("É um número inteiro")
    elif su != 0:
        print("É um número decimal")

if operacao == "3":
    divisao = num_1 / num_2
    print(divisao)
    div = divisao % 2
    print(div)
    di = divisao % 1
    print(di)
    
    if div == 0:
        print("Número par")
    elif div != 0:
        print("Número Impar")
    
    if divisao >= 0:
        print("Número Positivo")
    elif divisao < 0:
        print("Número Negativo")

    if di == 0:
        print("É um número inteiro")
    elif di != 0:
        print("É um número decimal")    

if operacao == "4":
    multiplicacao = num_1 * num_2
    mul = multiplicacao % 2
    mu = multiplicacao % 1
    
    if mul == 0:
        print("Número par")
    elif mul != 0:
        print("Número Impar")
    
    if multiplicacao >= 0:
        print("Número Positivo")
    elif multiplicacao < 0:
        print("Número Negativo")

    if mu == 0:
        print("É um número inteiro")
    elif mu != 0:
        print("É um número decimal")
