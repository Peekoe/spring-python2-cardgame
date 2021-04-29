#UnoClass

import random


class Card():
    #Class for each Uno Card

    def __init__(self, color:str, value:str):
        self.color = color
        self.value = value

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value


class Deck():

    def __init__(self):
        self.deck = []

    def populate_deck(self):
        """
        Creates the UNO deck with 108 cards.
        Two of each card except 0 which only has 1 copy
        """
        
        colors = ['Red','Green','Blue','Yellow']
        values = ['0','1','2','3','4', '5','6','7','8','9','Draw Two','Skip','Reverse']

        for color in colors:
            for value in values:
                temp_card = Card(color, value)
                self.deck.append(temp_card)

                #every card except 0 has 2 copies
                if value != '0':
                    self.deck.append(temp_card)

        for i in range(4):
            self.deck.append(Card('Wild',''))
            self.deck.append(Card('Wild','Draw Four'))

        
    def shuffle(self):
        """
        Shuffles the list of cards in the deck.
        """

        random.shuffle(self.deck)

    def add_card(self, card:Card):
        """
        Adds a card to the deck.
        """

        self.deck.append(card)

    def draw_card(self, num_cards) -> list:
        """
        Draws a number of cards from the top of the deck.
        Returns a list of cards drawn.
        """

        cards_drawn = []

        for i in range(num_cards):
            cards_drawn.append(self.deck.pop(0))

        return cards_drawn

    def print_deck(self):
        """
        Print all cards in deck for testing purposes.
        """

        for card in self.deck:
            print(card.get_color(), end = ' ')
            print(card.get_value())

    def top_card(self):
        """
        Returns the last card added in the deck
        """

        if not self.deck:
            return Card('Empty','')

        return self.deck[-1]


class Player():

    def __init__(self, number:int, hand:list):
        self.number = number
        self.hand = hand

    def add_cards(self, cards:list):
        """
        Adds cards to the Player's hand.
        """

        self.hand.extend(cards)


    def get_hand(self):
        return self.hand

    def show_hand(self):
        """
        Print player's hand
        """
        
        print("\nPlayer {}'s Hand".format(self.number + 1))

        i = 0
        
        for card in self.hand:
            print(i, end = ' - ')
            print(card.get_color(), end = ' ')
            print(card.get_value())

            i += 1

    def valid_play(self, top_color:str, top_value:str) -> bool:
        """
        Function determines whether the player can play a card or not.
        Returns True if there is a playable card in the player's hand.
        """

        if top_color == 'Empty':
            return True

        for card in self.hand:
            if card.get_color() == 'Wild' :
                return True
            elif card.get_color() == top_color or card.get_value() == top_value:
                return True

        return False

        
        
        
