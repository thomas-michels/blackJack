from blackjack import BlackJack
from jogador import Jogador


def jogar():
    bj = BlackJack()
    mesa = Jogador('Mesa')
    lista_jogadores = [mesa]
    print('#####  Bem vindo ao Black Jack  #####')
    jogadores = int(input('Insira quantos jogadores iram jogar: '))
    for i in range(0, jogadores):
        nome = input("Nome do Jogador: ")
        jogador = Jogador(nome)
        lista_jogadores.append(jogador)

    sair = False
    while not sair:
        for jogador in lista_jogadores:
            if jogador.get_venceu() is not True:
                jogada = bj.jogar(jogador)
                print(f'{jogador.nome} - Cartas: {jogador.cards}')

                if jogada is True:
                    print(f'{jogador.nome} venceu!')
                    sair = True
                    continue

                if jogador.nome == 'Mesa':
                    continue

                else:
                    opcao = input(f'Deseja continuar {jogador.nome}? S/N: ')
                    if opcao.upper() == 'N':
                        jogador.set_venceu(False)


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