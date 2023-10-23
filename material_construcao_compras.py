import os
piso = 15.90
cimento = 50.00
bloco_unidade = 1.00
pregos_centena = 5.00
areia_metro = 120.00
fios_elétricos = 3.00
parafusos_dezena = 1.00
tinta_litro = 85.00
tinta_18L = 150.00
verniz = 40.00

print("***************MATERIAIS DE CONSTRUÇÃO***************")
print("Bem-vindo a casa de Materiais de construção.")
resposta = int(input(f"Escolha uma opção abaixo.{os.linesep}[1] - Piso{os.linesep}[2] - Cimento{os.linesep}[3] - Bloco{os.linesep}[4] - Pregos{os.linesep}[5] - Areia{os.linesep}[6] - Fios elétricos{os.linesep}[7] - Parafusos{os.linesep}[8] - Tinta Lata 3.6{os.linesep}[9] - Tinta 18L{os.linesep}[10] - Verniz{os.linesep}"))
if resposta == 1:
    quantidade = float(input(f"Informe a metragem do piso: "))
    print(f"Você escolheu {quantidade} metros de piso, o valor foi de R${quantidade * piso: ,.2f}")
if resposta == 2:
    quantidade = int(input(f"Informe quantos sacos de cimentos vai levar: "))
    print(f"Você escolheu {quantidade} unidades de sacos de cimento, o valor foi de R${quantidade * cimento: ,.2f}")
if resposta == 3:
    quantidade = int(input(f"Informe a quantidade de blocos de deseja: "))
    print(f"Você escolheu {quantidade} centenas de blocos, o valor foi de R${quantidade * bloco_unidade: ,.2f}")
if resposta == 4:
    quantidade = int(input(f"Informe a quantidade de pregos que deseja: "))
    print(f"Você escolheu {quantidade} centenas de pregos, o valor foi de R${quantidade * pregos_centena: ,.2f}")
if resposta == 5:
    quantidade = float(input(f"Informe a metragem da areia: "))
    print(f"Você escolheu {quantidade} metros de areia, o valor foi de R${quantidade * areia_metro: ,.2f}")
if resposta == 6:
    quantidade = float(input(f"Informe a metragem de fios que deseja: "))
    print(f"Você escolheu {quantidade} metros de areia, o valor foi de R${quantidade * fios_elétricos: ,.2f}")
if resposta == 7:
    quantidade = int(input(f"Informe a quantidade de parafusos que deseja: "))
    print(f"Você escolheu {quantidade} dezenas de parafusos, o valor foi de R${quantidade * parafusos_dezena: ,.2f}")
if resposta == 8:
    quantidade = int(input(f"Informe quantas latas de tinta deseja: "))
    print(f"Você escolheu {quantidade} lata(s) de tinta de 3.6 litros, o valor foi de R${quantidade * tinta_litro: ,.2f}")
if resposta == 9:
    quantidade = int(input(f"Informe quantas latas de tinta deseja: "))
    print(f"Você escolheu {quantidade} lata(s) de tinta de 18 litros, o valor foi de R${quantidade * tinta_18L: ,.2f}")
if resposta == 10:
    quantidade = int(input(f"Informe quantas latas de Verniz deseja: "))
    print(f"Você escolheu {quantidade} lata(s) de Verniz de 1 litro, o valor foi de R${quantidade * verniz: ,.2f}")
else:
    print("Numero inválido!")


'''***************MATERIAIS DE CONSTRUÇÃO***************
Bem-vindo a casa de Materiais de construção.
Escolha uma opção abaixo.
[1] - Piso
[2] - Cimento
[3] - Bloco
[4] - Pregos
[5] - Areia
[6] - Fios elétricos
[7] - Parafusos
[8] - Tinta Lata 3.6
[9] - Tinta 18L
[10] - Verniz
10
Informe quantas latas de Verniz deseja: 2
Você escolheu 2 lata(s) de Verniz de 1 litro, o valor foi de R$ 80.00'''