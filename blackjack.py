from random import randint


class BlackJack:

    def __init__(self):
        self.__list_cards = [
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
        ]
        self.__dict_score_cards = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "A": 1,
            "J": 10,
            "Q": 10,
            "K": 10
        }
        self.__cards = []
        self.__score = 0
        self.__status = False
        self.__jogadas_restantes = 5

    def get_status(self):
        return self.__status

    def get_score(self):
        return self.__score

    def get_cards(self):
        return self.__cards

    def get_jogadas_restantes(self):
        return self.__jogadas_restantes

    def __calcular_score(self, carta):
        self.__score += self.__dict_score_cards[carta]

    def __retirar_carta_baralho(self, carta):
        self.__list_cards.remove(carta)

    def __adicionar_carta_mesa(self, carta):
        self.__cards.append(carta)

    def __validar_valor_a(self):
        if not self.__cards:
            self.__dict_score_cards["A"] = 11

    def get_card(self):
        indice = randint(0, (len(self.__list_cards) - 1))
        carta = self.__list_cards[indice]
        self.__jogadas_restantes -= 1
        self.__validar_valor_a()
        self.__retirar_carta_baralho(carta)
        self.__adicionar_carta_mesa(carta)
        self.__calcular_score(carta)
        return carta

    def jogar(self):
        print(f'Carta: {self.get_card()}')
        print(f'Cartas na Mesa: {self.get_cards()}')
        print(f'Score: {self.get_score()}')
        print(f'Jogadas Restantes: {self.get_jogadas_restantes()}')
