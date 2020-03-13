
class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.score = 0
        self.cards = []
        self.__jogadas_restantes = 5
        self.__venceu = None

    def set_jogadas(self, jogadas):
        self.__jogadas_restantes = jogadas

    def set_venceu(self, venceu):
        self.__venceu = venceu

    def set_cards(self, cards):
        self.__cards = cards

    def set_score(self, score):
        self.__score = score

    def get_jogadas(self):
        return self.__jogadas_restantes

    def get_venceu(self):
        return self.__venceu

    def get_cards(self) -> list:
        return self.__cards

    def get_score(self):
        return self.__score

    def __str__(self):
        return f'{self.nome};{self.__score};{self.__cards};{self.__jogadas_restantes};{self.__venceu}'
