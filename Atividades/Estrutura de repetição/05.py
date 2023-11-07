#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

popu_A = float(input("Informe a população atual da cidade: "))
popu_B = float(input("Informe a população atual da cidade: "))
taxa_cresc_A = float(input("Informe a taxa de crescimento: "))
txa = (taxa_cresc_A / 100)
taxa_cresc_B = float(input("Informe a taxa de crescimento: "))
txb = (taxa_cresc_B / 100)
ano = 0

while popu_A < popu_B:
    ano += 1
    popu_A = (popu_A * txa) + popu_A
    popu_B = (popu_B * txb) + popu_B
    if popu_A >= popu_B:
        print("População cidade A: %d\nPopulação cidade B: %d" % (popu_A, popu_B))
        print("Sendo assim serão necessarios {} anos para que a população da cidade A ultrapasse a população da cidade B".format(ano))
        
    else:           
        while popu_B <= popu_A:
            ano += 1
            popu_A = (popu_A * txa) + popu_A
            popu_B = (popu_B * txb) + popu_B
            if popu_A <= popu_B:
                print("População cidade A: %d\nPopulação cidade B: %d" % (popu_A, popu_B))
                print("Sendo assim serão necessarios {} anos para que a população da cidade A ultrapasse a população da cidade B".format(ano))            
                
continuar = str(input("Deseja Continuar?\nSim\nNão\n"))

if continuar == "sim":
    popu_A = float(input("Informe a população atual da cidade: "))
    popu_B = float(input("Informe a população atual da cidade: "))
    taxa_cresc_A = float(input("Informe a taxa de crescimento: "))
    txa = (taxa_cresc_A / 100)
    taxa_cresc_B = float(input("Informe a taxa de crescimento: "))
    txb = (taxa_cresc_B / 100)
    ano = 0

while popu_A < popu_B:
    ano += 1
    popu_A = (popu_A * txa) + popu_A
    popu_B = (popu_B * txb) + popu_B
    if popu_A >= popu_B:
        print("População cidade A: %d\nPopulação cidade B: %d" % (popu_A, popu_B))
        print("Sendo assim serão necessarios {} anos para que a população da cidade A ultrapasse a população da cidade B".format(ano))
    else:           
        while popu_B <= popu_A:
            ano += 1
            popu_A = (popu_A * txa) + popu_A
            popu_B = (popu_B * txb) + popu_B
            if popu_A <= popu_B:
                print("População cidade A: %d\nPopulação cidade B: %d" % (popu_A, popu_B))
                print("Sendo assim serão necessarios {} anos para que a população da cidade A ultrapasse a população da cidade B".format(ano)
            if popu_A <= popu_B:
                print("População cidade A: %d\nPopulação cidade B: %d" % (popu_A, popu_B))
                print("Sendo assim serão necessarios {} anos para que a população da cidade A ultrapasse a população da cidade B".format(ano))
