#TRIÂNGULOS

reta_A = float(input("Insira um valor da reta a: "))
reta_B = float(input("Insira um valor da reta b: "))
reta_C = float(input("Insira um valor da reta c: "))


if reta_A + reta_B > reta_C and reta_B + reta_C > reta_A and reta_A + reta_C > reta_B :
   print("Essas medidas formam um triângulo")

else:
    print("Essas medidas não podem formar um triângulo")


a = reta_A
b = reta_B
c = reta_C

if reta_A + reta_B > reta_C and reta_B + reta_C > reta_A and reta_A + reta_C > reta_B :

    if a == b and a == c and b == c:
        print("Esse é um triângulo equilatero")
    if a != b and a != c and b != c:
        print("Esse é um triângulo escaleno")
    if a == b != c or a == c != b or c == b != a:
        print("Esse é um triângulo Isósceles")
else:
    print("Não é um triângulo")