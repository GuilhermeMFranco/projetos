import random   

def jogar_dado():
    valor_min = 1
    valor_max = 6
    jogar_dado = random.randint(valor_min, valor_max)
    return jogar_dado

valor = jogar_dado()
print(valor)