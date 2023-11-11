import os

print("***************FEIRA LIVRE***************")

laranja_kg = 9.00
banana_kg = 6.50
batata_kg = 4.75
maca_kg = 8.49
pera_kg = 11.00
tomate_kg = 6.20
uva_kg = 9.62
abacaxi_kg = 6.25
melao_kg = 4.60
melancia_kg = 2.73
limao_kg = 4.25



info = input(f"Escolha as opções abaixo {os.linesep}[1] - Laranja {os.linesep}[2] - Bananas{os.linesep}[3] - Batata{os.linesep}[4] - Maça{os.linesep}[5] - Pera{os.linesep}[6] - Tomate{os.linesep}[7] - Uva{os.linesep}[8] - Abacaxi{os.linesep}[9] - Melão{os.linesep}[10] - Melancia{os.linesep}[11] - Limão{os.linesep}")
escolha = float(input("Quantos kilos vai levar? "))
if info == "1":
  print(f"Você escolheu {escolha} kilos de laranja, o valor da sua compra ficou R${laranja_kg * escolha: ,.2f}")
if info == "2":
  print(f"Você escolheu {escolha} kilos de Banana, o valor da sua compra ficou R${banana_kg * escolha: ,.2f}")
if info == "3":
  print(f"Você escolheu {escolha} kilos de Batata, o valor da sua compra ficou R${batata_kg * escolha: ,.2f}")
if info == "4":
  print(f"Você escolheu {escolha} kilos de Maça, o valor da sua compra ficou R${maca_kg * escolha: ,.2f}")
if info == "5":
  print(f"Voce escolheu {escolha} kilos de Pêra, o valor da sua compra ficou R${pera_kg * escolha: ,.2f}")
if info == "6":
  print(f"Você escolheu {escolha} kilos de Tomate, o valor da sua compra ficou R${tomate_kg * escolha: ,.2f}")
if info == "7":
  print(f"Você escolheu {escolha} kilos de Uva, o valor da sua compra ficou R${uva_kg * escolha: ,.2f}")
if info == "8":
  print(f"Você escolheu {escolha} kilos de Abacaxi, o valor da sua compra ficou R${abacaxi_kg * escolha: ,.2f}")
if info == "9":
  print(f"Você escolheu {escolha} kilos de Melão, o valor da sua compra ficou R${melao_kg * escolha: ,.2f}")
if info == "10":
  print(f"Você escolheu {escolha} kilos de Melancia, o valor da sua compra ficou R${melancia_kg * escolha: ,.2f}")
if info == "11":
  print(f"Você escolheu {escolha} kilos de Limão, o valor da sua compra ficou R${limao_kg * escolha: ,.2f}")
  
  
  
'''***************FEIRA LIVRE***************
Escolha as opções abaixo
[1] - Laranja
[2] - Bananas
[3] - Batata
[4] - Maça
[5] - Pera
[6] - Tomate
[7] - Uva
[8] - Abacaxi
[9] - Melão
[10] - Melancia
[11] - Limão
1
Quantos kilos vai levar? 0.500
Voce escolheu 0.5 kilos de laranja, o valor da sua compra ficou R$ 4.50'''
