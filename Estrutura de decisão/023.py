#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento

numero = float(input("Digite um número: "))


if numero % 1 == 0:
    print("O número {} é um número inteiro".format(int(numero)))

elif numero == 0:
    print("O número {} é um número neutro".format(numero))

else:
    print("O número {} é um número decimal".format(str(numero).replace('.',',')))