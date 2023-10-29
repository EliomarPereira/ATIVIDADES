#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    #"Telefonou para a vítima?"
    #"Esteve no local do crime?"
    #"Mora perto da vítima?"
    #"Devia para a vítima?"
    #"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada 
#como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


p_1 = str(input("Telefonou para a vítima sim ou não?\n")).upper()
p_2 = str(input("Esteve no local do crime?\n")).upper()
p_3 = str(input("Devia para a vitima?\n")).upper()
p_4 = str(input("Devia para a vítima?\n")).upper()
p_5 = str(input("Já trabalhou com a vítima?\n")).upper()

verdade = 0

if p_1 == "sim":
    verdade += 1

if p_2 == "sim":
    verdade += 1

if p_3 == "sim":
    verdade += 1

if p_4 == "sim":
    verdade += 1

if p_5 == "sim":
    verdade += 1


if verdade < 2:
    print("Inocente")
if verdade == 2:
    print("Suspeito")
if verdade == 3 or verdade == 4:
    print("Cúmplice")
else:
    print("Assassino")

   
 