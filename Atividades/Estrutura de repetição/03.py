#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


Feminino = "f"
Masculino = "m"

Solteiro = "1"
Casado = "2"
Viuvo = "3"
Divorciado = "4"

nome = str(input("Qual o seu nome?\n"))
nom = len(nome)
while nom < 3:
    nome = str(input("Qual o seu nome?\n"))
    nom = len(nome)
    continue
else:
    while nom >= 3:
        idade = int(input("Qual a sua idade?\n"))
        break
    
while idade < 0 or idade > 150:
    idade = int(input("Qual a sua idade?\n"))
    continue
else:
    while idade >= 0 and idade <= 150:
        salario = float(input("Qual é o seu salário?\n"))
        break    
    
sexo = input("Digite m para sexo masculino ou f para sexo feminino\nf - feminino\nm - masculino?\n")   
while sexo == Feminino or sexo == Masculino:
    estado_civil = str(input("Informe o seu estado civil:\n1 - Solteiro\n2 - Casado\n3 - viúvo\n4 - Divorciado\n"))
    break
else:
    while sexo != Feminino or sexo != Masculino:
        sexo = input("Digite m para sexo masculino ou f para sexo feminino\nf - feminino\nm - masculino?\n")
        break

        

