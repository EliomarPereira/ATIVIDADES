#CALCULA EQUAÇÃO DO SEGUNDO GRAU

a = int(input("Insira um valor: "))

if a == 0:
    print("Não é uma equação de segundo grau\nFIM!!!")
    exit()
else:
    b = int(input("Insira um valor: "))
    c = int(input("Insira um valor: "))


    delta = b ** 2 - (4 * a * c)


    if delta < 0:
        exit()
        print("A equação não possui raizes reais\nO programa será encerrado!!")

    elif  delta == 0:
        raiz_q = delta ** (1/2)
        x_1 = ((- b + raiz_q ) / ( 2 * a))
        x_2 = ((- b - raiz_q ) / ( 2 * a))
        print("{}\n{}\n{}".format(delta, x_1, x_2))
        print("A equação possui apenas uma raiz real !!")

    else:
        raiz_q = delta ** (1/2)
        x_1 = (- b + raiz_q ) / 2 * a
        x_2 = (- b - raiz_q ) / 2 * a
        print("{}\n{}\n{}".format(delta, x_1, x_2))
        print("A equação possui duas raizes reais !!")