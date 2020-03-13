from random import randint
from Baralho import Baralho
from score_cards import ScoreCards
from jogador import Jogador
from calcular_score import CalculadoraScore


class BlackJack:

    def __init__(self):
        self.__baralho = Baralho()
        self.__list_baralho = []
        self.__atualizar_baralho()
        score_cards = ScoreCards()
        self.__score_cards = score_cards.get_score_cards()
        self.__calculadora = CalculadoraScore()

    def __atualizar_baralho(self):
        self.__list_baralho = self.__baralho.get_baralho()

    def __retirar_carta_baralho(self, carta):
        self.__list_baralho.remove(carta)

    def __adicionar_carta(self, carta, jogador: Jogador):
        lista = jogador.get_cards()
        lista.append(carta)
        jogador.set_cards(lista)

    def __get_card(self):
        indice = randint(0, (len(self.__list_baralho) - 1))
        carta = self.__list_baralho[indice]
        return carta

    def __diminuir_jogada(self, jogador: Jogador):
        jogadas = jogador.get_jogadas()
        jogador.set_jogadas((jogadas - 1))

    def jogar(self, jogador: Jogador):
        if jogador.get_jogadas() < 1:
            jogador.set_venceu(False)
            return jogador.get_venceu()

        self.__diminuir_jogada(jogador)
        carta = self.__get_card()
        self.__retirar_carta_baralho(carta)
        self.__adicionar_carta(carta, jogador)
        self.__calculadora.calcular_score(jogador)

        return jogador.get_venceu()


