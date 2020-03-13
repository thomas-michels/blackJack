
class Baralho:

    def __init__(self):
        self.__baralho = []
        self.criar_baralho()

    def criar_baralho(self):
        self.__baralho = [
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            'A',
            'J',
            'Q',
            'K'
        ] * 4

    def get_baralho(self):
        return self.__baralho

    def set_baralho(self, baralho):
        self.__baralho = baralho
