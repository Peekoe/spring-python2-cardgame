CARDS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'R', '+2', '+4', 'S', 'A']


class Player:

    def __init__(self) -> None:
        self.hand = []
        self.handSize = len(self.hand)


class Card:

    def __init__(self, color, face) -> None:
        self.color = color
        self.face = face
