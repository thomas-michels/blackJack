from Data.score_cards import ScoreCards
from Model.jogador import Jogador


class CalculadoraScore:

    def __init__(self):
        obj = ScoreCards()
        self.__score_cards = obj.get_score_cards()

    def calcular_score(self, jogador: Jogador):
        score = 0
        lista_cartas_jogador = jogador.get_cards()

        for carta in lista_cartas_jogador:
            indice = lista_cartas_jogador.index(carta)
            if carta == 'A' and indice > 1:
                score += 1

            else:
                score += self.__score_cards[carta]

        jogador.set_score(score)

        if score == 21:
            jogador.set_venceu(True)
            jogador.set_jogar(False)

        elif score > 21:
            jogador.set_venceu(False)
