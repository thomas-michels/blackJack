from random import randint
from Data.Baralho import Baralho
from Data.score_cards import ScoreCards
from Model.jogador import Jogador
from Data.calcular_score import CalculadoraScore


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

    def verificar_jogadores_disponiveis(self, lista_jogadores: list) -> bool:
        for jogador in lista_jogadores:
            if jogador.get_jogar() is True and jogador.nome != 'Mesa':
                return True

        return False

    def verificar_ganhador(self, lista_jogadores: list) -> list:
        vencedor = []
        maior_score = 0
        for jogador in lista_jogadores:

            if jogador.nome != 'Mesa':
                if 22 > jogador.get_score() > maior_score:
                    if len(vencedor) > 0:
                        vencedor.pop(0)
                    vencedor.append(jogador)
                    maior_score = jogador.get_score()

                elif jogador.get_score() == maior_score:
                    vencedor.append(jogador)

        for jogador in vencedor:
            jogador.set_venceu(True)

        return vencedor

    def __validar_score(self, jogador: Jogador):
        if jogador.get_score() > 21:
            jogador.set_jogar(False)
            jogador.set_venceu(False)

        return jogador

    def jogar(self, jogador: Jogador):
        if jogador.get_jogadas() < 1:
            jogador.set_jogar(False)

        if jogador.get_jogar() is True:
            self.__diminuir_jogada(jogador)
            carta = self.__get_card()
            self.__retirar_carta_baralho(carta)
            self.__adicionar_carta(carta, jogador)
            self.__calculadora.calcular_score(jogador)

        self.__validar_score(jogador)
