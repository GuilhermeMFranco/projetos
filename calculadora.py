import os

primeiro_valor = float(input(f"Informe um valor para ser calculado: {os.linesep} [1] [2] [3] [/] {os.linesep} [4] [5] [6] [x] {os.linesep} [7] [8] [9] [-] {os.linesep} [#] [0] [*] [+]{os.linesep}"))
operacao = input("Escolha a operação desejada (+, -, *, /):")
segundo_valor = float(input("Escolha outro número: "))

if operacao == "+":
    resultado = primeiro_valor + segundo_valor
    print(f"Resultado: {resultado}")
elif operacao == "x":
    resultado = primeiro_valor * segundo_valor
    print("Operação inválida.")
elif operacao == "-":
    resultado = primeiro_valor - segundo_valor
    print("Operação inválida.")
elif operacao == "/":
    resultado = primeiro_valor / segundo_valor
    print(f"Resultado: {resultado}")
else:
    print("Operação inválida.")