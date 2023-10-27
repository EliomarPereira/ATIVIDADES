#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

vdd = False

#Válida se a data é verdadeira
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        vdd = True

elif mes == 4 or mes == 6 or mes == 9 or mes == 11 :
    if dia <= 30:
        vdd = True
elif mes == 2:
    if mes <= 28:
        vdd = True

if vdd:
    print("A data {} "" {} "" {}, é uma data válida".format(dia, mes, ano))

else:
    print("Data Inválida")

#Verifica se o ano é bissexto
ano_1 = ano // 4
resto = ano % 4
resto_1 = ano % 100
resto_2 = ano % 400

if vdd == True:
    if resto == 0 and resto_1 != 0:
        print("O ano de {} é um ano bissexto".format(ano))
        if resto != 0 and resto_2 == 0:
            print("O ano de {}  é um ano bissexto".format(ano))
    else:
        print("O ano de {} não é um ano bissexto".format(ano))
else:
    print("FIM !!!")