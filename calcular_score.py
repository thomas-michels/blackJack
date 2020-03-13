from score_cards import ScoreCards
from jogador import Jogador


class CalculadoraScore:

    def __init__(self):
        obj = ScoreCards()
        self.__score_cards = obj.get_score_cards()

    def calcular_score(self, jogador: Jogador):
        score = 0
        lista_cartas_jogador = jogador.get_cards()

        for carta in lista_cartas_jogador:
            if carta == 'A' and len(lista_cartas_jogador) > 2:
                score += 1

            else:
                score += self.__score_cards[carta]

        jogador.set_score(score)

        if score == 21:
            jogador.set_venceu(True)

        elif score > 21:
            jogador.set_venceu(False)
