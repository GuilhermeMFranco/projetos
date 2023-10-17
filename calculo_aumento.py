salario = float(input("Informe seu salário atual: "))
percentual = float(input("Informe seu aumento percentual: "))
novo_salario = salario +( salario *( percentual / 100))
total = novo_salario
print(f"Seu novo salário, com um aumento de {percentual}% será de: R${total: ,.2f} ")