nota = float(input("Nota: "))
nota_1 = float(input("Nota: "))
nota_2 = float(input("Nota: "))

media = (nota + nota_1 + nota_2) / 3
print("Média:{}".format(int(media)))

if media >= 7 and media <= 9.99:
    print("APROVADO")

elif media < 7 :
    print("REPROVADO")

else:
    print("APROVADO COM DISTINÇÃO")