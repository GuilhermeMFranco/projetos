print("**********NOTAS ESCOLARES**********\n")

nota_1 = int(input("Informe a nota do primeiro bimestre: "))
nota_2 = int(input("Informe a nota do segundo bimestre: "))
nota_3 = int(input("Informe a nota do terceiro bimestre: "))
nota_4 = int(input("Informe a nota do quarto bimestre: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7:
    print("Você foi aprovado.")
elif media >= 5 and media < 7:
    print("Você está de exame.")
else:
    print("Você foi reprovado.")