#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite uma nota de 0 a 10: "))

while nota > 10 or nota < 1:
    nota = float(input("Digite uma nota de 0 a 10: "))
    continue

else:
    while nota >=1 and nota <= 10:
        print("Nota válida")
        break