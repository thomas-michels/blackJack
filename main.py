from Model.blackjack import BlackJack
from Model.jogador import Jogador

def jogar():
    bj = BlackJack()
    mesa = Jogador('Mesa')
    lista_jogadores = [mesa]
    print('#####  Bem vindo ao Black Jack  #####')
    jogadores = int(input('Insira quantos jogadores irão jogar: '))
    for i in range(0, jogadores):
        nome = input("Nome do Jogador: ")
        jogador = Jogador(nome)
        lista_jogadores.append(jogador)

    sair = False

    bj.jogar(lista_jogadores[0])
    bj.jogar(lista_jogadores[0])
    cont_rodada = 1

    while not sair:
        for jogador in lista_jogadores:

            if bj.verificar_jogadores_disponiveis(lista_jogadores) is False:
                sair = True
                continue

            if jogador.nome == 'Mesa':
                continue

            bj.jogar(jogador)

            print(f'###  Rodada {cont_rodada}  ###')
            print(f'{lista_jogadores[0].nome} - Cartas: {lista_jogadores[0].cards[0]}')
            print(f'{jogador.nome} - Cartas: {jogador.cards} - Score: {jogador.get_score()}')
            print(f'Jogadas restantes: {jogador.get_jogadas()}')
            print('')

            if cont_rodada > 1:
                if jogador.get_jogar() is True:
                    opcao = input(f'Deseja continuar {jogador.nome}? S/N: ')

                    if opcao.upper() == 'N':
                        jogador.set_jogar(False)

        cont_rodada += 1

    if lista_jogadores[0].get_score() < 17:
        bj.jogar(lista_jogadores[0])

    ganhador = bj.verificar_ganhador(lista_jogadores)

    print('#' * 50)
    print(f'{lista_jogadores[0].nome} - Cartas: {lista_jogadores[0].get_cards()} - Score: {lista_jogadores[0].get_score()}')

    if len(ganhador) > 1:
        print('Empate')
        print(ganhador)

    else:
        print(f'{ganhador[0].nome} ganhou com o score {ganhador[0].get_score()} e com as cartas {ganhador[0].get_cards()}')


if __name__ == '__main__':
    jogar()
