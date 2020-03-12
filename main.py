from blackjack import BlackJack
import os


def jogar():
    bj = BlackJack()

    print('### Bem Vindo ao BLACKJACK ###')
    opcao = input("Iniciar jogo? S/N: ")

    if opcao.upper() == 'N':
        return ''

    os.system('cls')
    bj.jogar()
    print("")
    bj.jogar()

    status = False
    while not status:
        print("")
        status = bj.get_status()
        if status:
            continue

        opcao = input("Continuar jogo? S/N: ")
        if opcao.upper() == 'S':
            bj.jogar()

        else:
            break


if __name__ == '__main__':
    jogar()