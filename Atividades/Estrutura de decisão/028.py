#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                #Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por K
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
#Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne 
#comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipo_carne = str(input("Escolha um tipo de carne\n1 - File Duplo\n2 - Alcatra\n3 - Picanha\n"))
quantidade = float(input("Quantidade que deseja comprar: "))
forma_pagamento = str(input("Qual será a forma de pagamento?\n1 - cartão tabajara\n2 - Á vista\n"))

#Tipos de Carne
if tipo_carne == "1":
    carne = "Filé Duplo"
if tipo_carne == "2":
    carne = "Alcatra"
if tipo_carne == "3":
    carne = "Picanha"

#Formas de Pagamento
cartao_tabajara = "1"
a_vista = "2"
if forma_pagamento == "1":
    tipo_pagamento = "Cartão Tabajara"
elif forma_pagamento == "2":
    tipo_pagamento = "Á vista"

#Faixas de preço por Kg
if quantidade <= 5:
    file_duplo = 4.90
    Alcatra = 5.90
    Picanha = 6.90

elif quantidade > 5:
    file_duplo = 5.80
    Alcatra = 6.80
    Picanha = 7.80


#File Duplo
if tipo_carne == "1":
    if forma_pagamento == "1":
        valor_total = file_duplo * quantidade
        desconto = valor_total * 0.05
        valor_a_pagar = valor_total - desconto
        print("Tipo de Carne: {}\nQuantidade: {}\nValorTotal: {:.2f}\nTipo de pagamento: {}\nDesconto: {:.2f}\nValor a pagar: {:.2f}".format(carne, quantidade,valor_total, tipo_pagamento, desconto, valor_a_pagar))

    if forma_pagamento == "2":
        valor_total = file_duplo * quantidade
        valor_a_pagar = valor_total
        print("Tipo de Carne: {}\nQuantidade: {}\nValorTotal: {:.2f}\nTipo de pagamento: {}\nValor a pagar: {:.2f}".format(carne, quantidade,valor_total, tipo_pagamento, valor_a_pagar))
#Alcatra
if tipo_carne == "2":
    if forma_pagamento == "1":
        valor_total = Alcatra * quantidade
        desconto = valor_total * 0.05
        valor_a_pagar = valor_total - desconto
        print("Tipo de Carne: {}\nQuantidade: {} Kg\nValorTotal: {:.2f} R$\nTipo de pagamento: {}\nDesconto: {:.2f} R$\nValor a pagar: {:.2f} R$".format(carne, quantidade,valor_total, tipo_pagamento, desconto, valor_a_pagar))

    if forma_pagamento == "2":
        valor_total = Alcatra * quantidade
        valor_a_pagar = valor_total
        print("Tipo de Carne: {}\nQuantidade: {} Kg\nValorTotal: {:.2f} R$\nTipo de pagamento: {} R$\nValor a pagar: {:.2f} R$".format(carne, quantidade,valor_total, tipo_pagamento, valor_a_pagar))

#Picanha
#Alcatra
if tipo_carne == "3":
    if forma_pagamento == "1":
        valor_total = Picanha * quantidade
        desconto = valor_total * 0.05
        valor_a_pagar = valor_total - desconto
        print("Tipo de Carne: {}\nQuantidade: {} Kg\nValorTotal: {:.2f} R$\nTipo de pagamento: {}\nDesconto: {:.2f} R$\nValor a pagar: {:.2f} R$".format(carne, quantidade,valor_total, tipo_pagamento, desconto, valor_a_pagar))

    if forma_pagamento == "2":
        valor_total = Picanha * quantidade
        valor_a_pagar = valor_total
        print("Tipo de Carne: {}\nQuantidade: {} Kg\nValorTotal: {:.2f} R$\nTipo de pagamento: {} R$\nValor a pagar: {:.2f} R$".format(carne, quantidade,valor_total, tipo_pagamento, valor_a_pagar))
    