print("Bem-vindo ao QUIZGAME \n")

jogo = input("vamos jogar? ")
if jogo.lower() != "sim":
    quit()
else:
    print("Ótimo! Vamos começar.\n")

score = 0

print("Qual é o país mais populoso do mundo? \n")
print("Escolha uma das alternativas abaixo.")
pergunta = input(
    "a) India\n"
    "b) Indonésia\n"
    "c) Estados Unidos\n"
    "d) China\n"
).lower()

if pergunta.lower() == "a":
    print("Você acertou!")
    score += 1
else:
    print("Você errou!")

print("qual é o maior oceano do mundo?")
pergunta = input(
    "a) Ártico\n"
    "b) Pacífico\n"
    "c) Atlântico\n"
    "d) Índico\n"
).lower()

if pergunta.lower() == "b":
    print("Você acertou!")
    score += 1
else:
    print("Você errou!")

print("qual é a capital do Brasil?")
pergunta = input(
    "a) São paulo\n"
    "b) Rio de Janeirio\n"
    "c) Maringá\n"
    "d) Brasília\n"
).lower()

if pergunta.lower() == "d":
    print("Você acertou!")
    score += 1
else:
    print("Você errou! \n")

print("Qual é o rio mais longo do mundo?")
pergunta = input(
    "a) Rio Amazonas\n"
    "b) Rio Nilo\n"
    "c) Rio Danubio\n"
    "d) Rio Paraná\n"
).lower()

if pergunta.lower() == "b":
    print("Você acertou!")
    score += 1
else:
    print("Você errou!")

print("Qual é a montanha mais alta do mundo?")
pergunta = input(
    "a) Makalu\n"
    "b) Pico de Jaragua\n"
    "c) Monte Everest\n"
    "d) K2\n"
).lower()

if pergunta.lower() == "c":
    print("Você acertou!")
    score += 1
else:
    print("Você errou!")

print("Que deserto é o maior do mundo?")
pergunta = input(
    "a) Atacama\n"
    "b) Patagônia\n"
    "c) Saara\n"
    "d) Arizona\n"
).lower()

if pergunta.lower() == "c":
    print("Você acertou!")
    score += 1
else:
    print("Você errou!")

print("Qual é o país conhecido como A Terra dos Cangurus?")
pergunta = input(
    "a) Japão\n"
    "b) Canada\n"
    "c) França\n"
    "d) Autrália\n"
).lower()

if pergunta.lower() == "d":
    print("Você acertou!")
    score += 1
else:
    print("Você errou!")

print("Qual é o menor país do mundo?")
pergunta = input(
    "a) Japão\n"
    "b) Portugal\n"
    "c) Vaticano\n"
    "d) Israel\n"
).lower()

if pergunta.lower() == "c":
    print("Você acertou!")
    score += 1
else:
    print("Você errou!")

print("Parabéns! você fez " + str(score) + " pontos.")
