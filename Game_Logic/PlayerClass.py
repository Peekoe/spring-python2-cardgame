#Player Class.py

#Eriq Deng 4/8/2021

class Card(): #incomplete
    #Base class for any type of card

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Monster(Card): #incomplete
    #Class for a Monster type card

    def __init__(self, name, stars, attack, defense):
        self.name = name
        self.stars = stars
        self.attack = attack
        self.defense = defense

class Spell(Card): #incomplete
    #Class for a Spell Card

    def __init__(self, name, effects):
        self.name = name
        self.effects = effects
    
class Trap(Card): #incomplete
    #Class for a Trap Card

    def __init__(self, name, effects):
        self.name = name
        self.effects = effects

class Lifepoints():

##    Class for handling a player's lifepoint total
##
##    Methods:
##    increase(self,amount)
##    decrease(self,amount)
##    get_lifepoints(self)

    def __init__(self, lifepoints):
        self.lifepoints = lifepoints

    def increase(self, amount):
        self.lifepoints = self.lifepoints + amount

    def decrease(self, amount):
        self.lifepoints = self.lifepoints - amount

    def get_lifepoints(self):
        return self.lifepoints
    
     

class Stack():
##    Class for handling a player's hand, deck, or graveyard
##
##    Methods:
##    add_card(self,card)
##    remove_card(self,card)
##    list_cards(self)
##    get_card(self, pos)
##    get_count(self)

    def __init__(self, name, stack_list = None):
        """
        Constructor takes name and stackList if available
        """
        self.name = name

        #if there is no stackList provided, self.list is an empty list
        if stack_list == None:
            self.list = []
            self.count = 0
        else:
            self.list = list(stack_list)
            self.count = len(stack_list)

    def add_card(self, card):
        """
        Adds card to self.list
        """

        self.list.append(card)
        self.count += 1
        print("{0} was added to {1}".format(card.get_name(), self.name))
        

    def remove_card(self, card):
        """
        Removes a card from self.list
        """

        self.list.remove(card)
        self.count -= 1
        print("{0} was removed from {1}".format(card.get_name(), self.name))

    def list_cards(self):
        """
        Shows all cards in the stack
        """

        if len(self.list) == 0:
            print("{} is empty!".format(self.name))
        else:
            for card in self.list:
                print(card.get_name())

        

    def get_card(self, pos = 0):
        """
        Returns card at position in self.list. if no pos given, return first card
        """
        return self.list[pos]
    
            
    def get_count(self):
        """
        Returns a count of all cards in stack
        """
        return self.count

    


class Player():
##    Player Class
##
##    Methods:
##    draw(self)
##
    def __init__(self, name, decklist):
        self.name = name
        self.hand = Stack("{}'s Hand".format(self.name))
        self.deck = Stack("{}'s Deck".format(self.name), decklist)
        self.graveyard = Stack("{}'s Graveyard".format(self.name))
        self.lifepoints = Lifepoints(8000)

    def draw(self): #currently draws top card of deck
        """
        Adds a card from the deck list to the player's hand
        """

        deck_count = self.deck.get_count()

        if deck_count > 0:
            drawn_card = self.deck.get_card()
            self.deck.remove_card(drawn_card)
            self.hand.add_card(drawn_card)
        else:
            print("Your deck is empty.")

def testing():
    """
    Function for testing Player class
    """


    test_card_1 = Monster("Blue Eyes White Dragon", 8, 3000, 2500)
    test_card_2 = Monster("Kuriboh", 1, 300, 200)
    test_card_3 = Monster("Dark Magician", 7, 2500, 2100)
    
    test_deck_list = [test_card_1, test_card_2, test_card_3]


    print("Welcome to the Yu-Gi-Oh! simulator by Eriq Deng \n")

    player_name = str(input("Please enter your name: "))

    player_one = Player(player_name, test_deck_list)

    print("\nCurrently, you start with an empty hand and 3 test cards in the deck to draw.\nYou start with 8000 lifepoints and can edit the player's lifepoints as well.\n")    
    print("Press 1 to view your hand")
    print("Press 2 to draw a card")
    print("Press 3 to view your lifepoints")
    print("Press 4 to change your lifepoints")
    print("Press 5 to exit the simulator")

    choice = 0
    
    while choice != 5:
        while True:
            try:
                choice = int(input("Please choose a menu option: "))
            except:
                print("Sorry, that is not a valid option.")
                continue
            if choice < 1 or choice > 5:
                print("Sorry, that is not a valid option.")
                continue
            break

        if choice == 1:
            player_one.hand.list_cards()

        elif choice == 2:
            player_one.draw()

        elif choice == 3:
            print(player_one.lifepoints.get_lifepoints())

        elif choice == 4: 
            while True:
                try:
                    life_choice = int(input("Enter 1 to increase lifepoints or 2 to decrease lifepoints: "))
                except:
                    print("Sorry, that is not a valid option.")
                    continue
                if life_choice < 1 or life_choice > 2:
                    print("Sorry, that is not a valid option.")
                    continue
                break

            while True:
                try:
                    life_amount = int(input("Enter the amount you would like to increase/decrease: "))
                except:
                    print("Sorry, that is not a valid option.")
                    continue
                break

            if life_choice == 1:
                player_one.lifepoints.increase(life_amount)
                print("{0} lifepoints were added to {1}'s total lifepoints.".format(life_amount, player_one.name))

            elif life_choice == 2:
                player_one.lifepoints.decrease(life_amount)
                print("{0} lifepoints were removded from {1}'s total lifepoints.".format(life_amount, player_one.name))

        elif choice == 5:
            print("Exiting program!")
            


if __name__ == '__main__':
    testing()
