UNO README - by Eriq, Charlie, and Derrek

This a test version of our project titled UnoGame. There are two files UnoClass.py and UnoGameFunctions.py. UnoClass is a module that
contains the classes used for the game. Run UnoGameFunctions.py to play the game. As of now, the game is fully text-based but we will
be working with PyGame in the future to add GUI elements to it. For now, we would like to test the game logic itself to make 
sure that all of the rules and cards work appropriately. Most of the testing should be done through playing the game itself.

Main things to test:
1) valid_play() function in Player class:
	This function determines whether or not a player can play a card on the turn they have. If it returns True, then the Player
	will be prompted to play a card. If it returns False, then the player will be forced to draw a card. We would like to make sure
	that the player is able to play a card whenever they have an available card.
	
2) choose_card() function in UnoGameFunctions:
	This function is the function called when the player needs to choose a card to be played. There is some try/except stuff here to
	ensure that the card being played is allowed to be played according to the rules. Try testing out cards that can't be played and make
	sure that the exceptions are handled properly.
	
3) Winning the game:
	The last thing to test is actually just the win condition on the game. Also making sure that the deck does not return an error if the 
	game happens to last too long. The deck should repopulate and shuffle again if the deck runs out of cards without the game being over.
