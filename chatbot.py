import os


def adicionar_resposta(resposta, nome):
    if resposta == '1':
        print(
            f'{os.linesep}{nome} Fazemos serviços de Alongamento de unha, Banho em gel, manicure e Pédicure .{os.linesep}')
    elif resposta == '2':
        print(
            f'{os.linesep}{nome}, estamos localizado na Rua Juvenal Gomes do Monte, 59 - centro - Franco da Rocha - SP.{os.linesep}')
    elif resposta == '3':
        print(
            f'{os.linesep}{nome}, https://whatsapp.com..{os.linesep}')
    elif resposta == '4':
        print(
            f'{os.linesep}{nome} https://www.webprospector.com.br/wp-content/uploads/2020/12/design-unhas-09.jpg{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresentar o chatbot
    print(f'Olá! Bem-vindo ao Studio Daiane Franco')
    # pedir o nome
    nome = input('Qual é o seu nome por gentileza? ')

    while True:
        # Oferer o menu de opções
        resposta = input(
            f'Escolha uma das opções.{os.linesep}[1] - Nossos serviços{os.linesep}[2] - Nossa localização{os.linesep}[3] - Agendamento{os.linesep}[4] - Portfolio{os.linesep}')
        # Processar a resposta enviada
        adicionar_resposta(resposta, nome)


if __name__ == '__main__':
    start()