import os

print("***************CALCULADORA PYTHON***************")
primeiro_valor = int(input(f"Informe o primeiro valor da operação:{os.linesep}[1] [2] [3] [/]{os.linesep}[4] [5] [6] [*]{os.linesep}[4] [5] [6] [-]{os.linesep}[7] [8] [9] [+] {os.linesep}[*] [0] [#] [=]{os.linesep }"))
operacao = input("Escolha um operação matemática: (+, -, *, /)")
segundo_valor = int(input("Escolha o segundo valor da operação: "))

if operacao == "+":
    resultado = primeiro_valor + segundo_valor
    print(f"Resultado: {resultado}")
if operacao == "-":
    resultado = primeiro_valor - segundo_valor
    print(f"Resultado: {resultado}")
if operacao == "*":
    resultado = primeiro_valor * segundo_valor
    print(f"Resultado: {resultado}")
if operacao == "/":
    resultado = primeiro_valor / segundo_valor
    print(f"Resultado: {resultado}")


'''***************CALCULADORA PYTHON***************
Informe o primeiro valor da operação:
[1] [2] [3] [/]
[4] [5] [6] [*]
[4] [5] [6] [-]
[7] [8] [9] [+]
[*] [0] [#] [=]
10
Escolha um operação matemática: (+, -, *, /)*
Escolha o segundo valor da operação: 10
Resultado: 100'''
