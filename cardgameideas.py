'''
Trading card game thing
'''


class Player:
    pass

class UnoCard:
    COLORS = ['r', 'g', 'y', 'b']
    VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, setValue=0, setColor='') -> None:
        self.value = setValue
        self.color = setColor
        assert self.color in self.COLORS

class ReverseCard(UnoCard):
    pass

class DrawCard(UnoCard):
    pass

class SkipCard(UnoCard):
    pass

'''
card types:
monster/creature
spells
mana(?) or maybe do per turn hearthstone mana
'''

'''
magic:
creatures
 -attributes like: lifesteal, haste, trample
spells/instants/enchantments
land
planeswalkers
weapons

pokemon:
pokemon
items?
energy

yugioh:
monsters
spell cards
trap cards
'''

'''
unos rules:
match color or face value
skip 1 person for skip card
switch changes turn order
+2 and skip turn/+4 and change color
any color
double stack if same card (optional)
0 and 7's rules (optional)
draw until you can play (optional)
'''
