
class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.score = 0
        self.cards = []
        self.__jogadas_restantes = 5
        self.__venceu = None
        self.__jogar = True

    def set_jogar(self, jogar):
        self.__jogar = jogar

    def set_jogadas(self, jogadas):
        self.__jogadas_restantes = jogadas

    def set_venceu(self, venceu):
        self.__venceu = venceu

    def set_cards(self, cards):
        self.cards = cards

    def set_score(self, score):
        self.score = score

    def get_jogar(self):
        return self.__jogar

    def get_jogadas(self):
        return self.__jogadas_restantes

    def get_venceu(self):
        return self.__venceu

    def get_cards(self) -> list:
        return self.cards

    def get_score(self):
        return self.score
