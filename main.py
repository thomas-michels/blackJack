from blackjack import BlackJack
from jogador import Jogador

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
    indice = 0
    while not sair:

        cont_jogador = 0
        for jogador in lista_jogadores:
            if jogador.nome != 'Mesa':
                if jogador.get_jogar() is False:
                    cont_jogador += 1

        if (cont_jogador + 1) == len(lista_jogadores):
            mesa = lista_jogadores[0]
            if mesa.get_score() < jogador.get_score() and mesa.get_score() < 17:
                bj.jogar(mesa)

            sair = True
            continue

        if indice > (len(lista_jogadores) - 1): # Verificação de indice dentro da lista
            indice = 0

        jogador = lista_jogadores[indice]

        if jogador.get_venceu() is True:
            print(f'{jogador.nome} Venceu com o score {jogador.score}')
            sair = True
            continue

        if jogador.nome == 'Mesa':
            indice += 1
            continue

        if jogador.get_jogar() is True:
            bj.jogar(jogador)

        print(f'{lista_jogadores[0].nome} - Cartas: {lista_jogadores[0].cards[0]}')
        print(f'{jogador.nome} - Cartas: {jogador.cards} - Score: {jogador.score} - Jogadas Restantes: {jogador.get_jogadas()}')

        opcao = input(f'Deseja continuar {jogador.nome}? S/N: ')
        if opcao.upper() == 'N':
            jogador.set_jogar(False)

        indice += 1

    ganhador = bj.verificar_ganhador(lista_jogadores)
    print(ganhador)
    print(ganhador.nome + " ganhou")

if __name__ == '__main__':
    jogar()
    # b = BlackJack()
    # j1 = Jogador("a")
    # j2 = Jogador('b')
    # b.jogar(j1)
    # b.jogar(j2)
    # print(j1)
    # print(j2)
    # b.jogar(j1)
    # print(j1)
    # print(j2)