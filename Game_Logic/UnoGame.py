#UnoGame.py

import random
from UnoClass import Card, Deck, Player

def uno_game():
    
    uno_deck = Deck();
    uno_deck.populate_deck()
    uno_deck.shuffle()

    discard_pile = Deck();

    players = []
    colors = ['Red','Blue','Green','Yellow']

    while True:
        try:
            num_players = int(input("Please enter the number of players between 2 and 4: "))
        except:
            print("Please enter a valid number.")
            continue
        if num_players < 2 or num_players > 4:
            print("Please enter a number between 2 and 4.")
            continue
        break
        
    #initialize each player with a hand of 5 cards
    for i in range(num_players):
        players.append(Player(i, uno_deck.draw_card(5)))

    player_turn = 0
    play_order = 1
    game_end = False

    current_color = 'Empty'
    current_value = ''
    
    while not game_end:

        players[player_turn].show_hand()

        print("Current card on top of discard pile: {} {}".format(current_color, current_value))

        if players[player_turn].valid_play(current_color, current_value):
            while True:
                try:
                    card_choice = int(input("Please choose a card to play: "))
                    played_card = players[player_turn].get_hand()[card_choice]
                except:
                    print("Please enter a valid number.")
                    continue
                if card_choice < 0 or card_choice > len(players[player_turn].get_hand()) - 1:
                    print("Please enter a valid choice.")
                    continue
                if played_card.get_color() != current_color and played_card.get_value() != current_value and current_color != 'Empty' and played_card.get_color() != 'Wild':
                    print("You can't play this card.")
                    continue
                
                break

            discard_pile.add_card(players[player_turn].get_hand().pop(card_choice))

            current_color = discard_pile.top_card().get_color()
            current_value = discard_pile.top_card().get_value()

            #Handle wild card color
            if current_color == 'Wild':
                print("1 - Red\n2 - Blue\n3 - Green\n4 - Yellow")

                while True:
                    try:
                        color_choice = int(input("Choose a color: "))
                    except:
                        print("Please enter a valid number.")
                        continue
                    if color_choice < 1 or num_players > 4:
                        print("Please enter a number between 2 and 4.")
                        continue
                    break

                if color_choice == 1:
                    current_color = 'Red'
                elif color_choice == 2:
                    current_color = 'Blue'
                elif color_choice == 3:
                    current_color = 'Green'
                elif color_choice == 4:
                    current_color = 'Yellow'

            #Check for reverse
            if current_value == 'Reverse':
                play_order = play_order * -1

            #Check for skip turn
            elif current_value == 'Skip':
                player_turn += play_order
                if player_turn == num_players:
                    player_turn = 0
                elif player_turn < 0:
                    player_turn = num_players - 1

            #Check for Draw Two
            elif current_value == 'Draw Two':
                player_draw = player_turn + play_order

                if player_draw == num_players:
                    player_draw = 0
                elif player_turn < 0:
                    player_draw = num_players - 1

                players[player_draw].add_cards(uno_deck.draw_card(2))

            #Check for Draw four
            elif current_value == 'Draw Four':
                player_draw = player_turn + play_order

                if player_draw == num_players:
                    player_draw = 0
                elif player_turn < 0:
                    player_draw = num_players - 1

                players[player_draw].add_cards(uno_deck.draw_card(4))


        else:
            print("You have no available cards to play. Draw a card.")
            players[player_turn].add_cards(uno_deck.draw_card(1))

        #game ends and there is a winner if hand reaches 0
        if len(players[player_turn].get_hand()) == 0:
            game_end = True
            

        


        
       #move to next player's turn 
        player_turn += play_order

        #loop around to first player 
        if player_turn == num_players:
            player_turn = 0
        elif player_turn < 0:
            player_turn = num_players - 1

           
    print("Game over.")



        

        

    

    
    
if __name__ == '__main__':
    uno_game()
