#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule
# e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


produto = str(input("Qual o tipo de combustivel abastecido(G - gasolina ou A - álcool): ")).upper()
quantidade = float(input("Quantidade abastecida: "))

gasolina = "G"
alcool = "A"
valor_gas = 2.50
valor_alcool = 1.90

if produto == gasolina:
    if quantidade <= 20 :
        valor_a_pagar = quantidade * valor_gas
        valor_total = valor_a_pagar * 0.04 
        valor_total_desconto = valor_a_pagar - valor_total
        print("Valor a ser pago {:.2f} R$".format(valor_total_desconto))
    if quantidade > 20 :
        valor_a_pagar = quantidade * valor_gas
        valor_total = valor_a_pagar * 0.06 
        valor_total_desconto = valor_a_pagar - valor_total
        print("Valor a ser pago {:.2f} R$".format(valor_total_desconto))
else:
    if quantidade < 20 :
        valor_a_pagar = quantidade * valor_alcool 
        print("Valor a ser pago {:.2f} R$".format(valor_a_pagar))
    if quantidade >= 20 :
        valor_a_pagar = quantidade * valor_alcool
        valor_total = valor_a_pagar * 0.05 
        valor_total_desconto = valor_a_pagar - valor_total
        print("Valor a ser pago {:.2f} R$".format(valor_total_desconto))
