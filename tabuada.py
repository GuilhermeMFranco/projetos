tabuada = True
while tabuada == True:
    tab = int(input("Informe a tabuada que deseja consultar: "))
    for n in range(1, 11):
        print(n, " x ", tab, " = ", tab * n)
    resp = input("Deseja relizar outra consulta? Se sim digite 'S' ou 'N' se não deseja: ")
    if resp.lower() == "n":
        tabuada = False