num = int(input("Informe um número: "))

cen = num // 100
dez = num % 100 // 10
unid = num // 1 % 10
dezena = num % 10 // 10

if cen <= 1:
    if dez <= 1:
        if unid <= 1:
            print("{} = {} centena, {} dezena e {} unidade".format(num, cen, dez, unid))

if cen == 1:
    if dez >= 2:
        if unid >= 2:
            print("{} = {} centena, {} dezenas e {} unidades".format(num, cen, dez, unid))

if cen <= 1:
    if dez >= 2:
        if unid <= 1:
            print("{} = {} centena, {} dezenas e {} unidade".format(num, cen, dez, unid))

if cen >= 2 or cen == 0:
        if dez >= 2 or dez == 0:
            if unid >= 2:
                print("{} = {} centenas, {} dezenas e {} unidades".format(num, cen, dez, unid))

if cen >= 2:
    if dez <= 1:
        if unid <= 1 :
            print("{} = {} centenas, {} dezena e {} unidade".format(num, cen, dez, unid))

if cen >= 2 or cen == 0:
    if dez <= 1:
        if unid >= 2:
            print("{} = {} centenas, {} dezena e {} unidades".format(num, cen, dez, unid))

if cen >= 2:
    if dez >= 2:
        if unid == 0:
            print("{} = {} centenas, {} dezenas e {} unidade".format(num, cen, dez, unid))
