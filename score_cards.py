
class ScoreCards:

    def __init__(self):
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
            "A": 11,
            "J": 10,
            "Q": 10,
            "K": 10
        }

    def get_score_cards(self):
        return self.__dict_score_cards