print("**********CALCULO DE METRAGEM DE PISO**********")

pergunta1 = float(input("Informe a metragem da altura da parede: "))
pergunta2 = float(input("Informe a metragem da largura da parede: "))
conta = pergunta1 * pergunta2
roda_pe = (conta * 1.10)
percent = round(roda_pe / 4, 1)
print(f"Sua parede mede {conta} metros quadrado.")
print(f"Você precisa de {conta} metros quadrado de piso e mais {percent} metros para o rodapé. ")
argamassa = int(conta / 4)
percent1 = int(percent * 1.10) / 4
result = argamassa + percent1
print(f"Você irá usar no total {result} sacos de argamassa. ")
