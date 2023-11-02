#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = str(input("Usuário: "))
senha = (input("A sua senha é igual ao nome de usuário: "))

while senha == usuario:
    print("SEJA BEM VINDO !!!")
    break

else:
    while senha != usuario:
        usuario = str(input("Usuário: "))
        senha = str(int(input("A sua senha é igual ao nome de usuário")))
        continue
