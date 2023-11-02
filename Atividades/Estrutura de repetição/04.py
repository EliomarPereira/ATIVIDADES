#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
#com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que 
#a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.


popu_A = 80000
popu_B = 200000
taxa_cresc_A = 0.03
taxa_cresc_B = 0.015
ano = 0

while popu_A < popu_B:
    ano += 1
    popu_A = (popu_A * taxa_cresc_A) + popu_A
    popu_B = (popu_A * taxa_cresc_B) + popu_B
    if popu_A >= popu_B:
        print("População cidade A: %d\nPopulação cidade B: %d" % (popu_A, popu_B))
        print("Sendo assim serão necessarios {} anos para que a população da cidade A ultrapasse a população da cidade B".format(ano))
