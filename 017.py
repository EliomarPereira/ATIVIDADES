num = int(input("Informe o ano: "))

ano = num // 4
resto = num % 4
resto_1 = num % 100
resto_2 = num % 400

if resto == 0 and resto_1 != 0:
    print("O ano de {} é uma ano bissexto".format(num))
    if resto != 0 and resto_2 == 0:
        print("O ano de {} de é uma ano bissexto".format(num))
else:
    print("O ano de {} não é um ano bissexto".format(num))