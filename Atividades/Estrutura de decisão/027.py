#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                    #Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para 
#ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

maca = float(input("Qual foi a quantidade de maçãs compradas(em Kg): "))
morango = float(input("Qual foi a quantidade de morangos comprados (em Kg): "))

peso_frutas = maca + morango



if morango < 5:
    valor_morango = 2.50
if morango >= 5:
    valor_morango = 2.20
if maca < 5:
    valor_maca = 1.8
if maca >= 5:
    valor_maca = 1.50


valor_total = (morango * valor_morango) + (maca * valor_maca)

if valor_total >= 25 or peso_frutas >= 8:
    total_maca = (maca * valor_maca) * 0.1
    total_morango = (morango * valor_morango) * 0.1
    valor_desconto = (morango * valor_morango) + (maca * valor_maca) - total_morango - total_maca
    print("Valor total da compra foi {:.2f} R$".format(valor_desconto))

else:
   valor_sem_desconto = (morango * valor_morango) + (maca * valor_maca)
   print("Valor total da compra foi {:.2f} R$".format(valor_sem_desconto))