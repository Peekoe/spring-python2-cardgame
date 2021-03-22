# Group Members: Charlie, Mauricio, Derrek, Eriq

import pygame
from pygame.locals import *

print("\n Welcome to the UI of YuGiOh Verison 0.3!")
print("The main screen of play.")
print("Players will be using this screen during battle.")
print("Added feature apart from the GUI is the ability to summon")
print("cards in hand from moving cursor towards the bottom")
print("\n Still working with sprites in order to have them move around")
print("While also being able to remove the cards from screen once cursor")
print("is moved from the area.")

hand = []
handCoordinates = [(150, 850),(300, 850),(450, 850),
                      (600, 850),(750, 850),(900, 850)]
show_hand = False

class YuGiOhCardSprite(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.inHand = True
        
        self.image = pygame.image.load(picture_path).convert()
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        hand.append(self)

    def update(self):
        self.rect.center = handCoordinates[hand.index(self)]
        if show_hand is True:
            self.kill()
            
    

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200,1000))

# Yu Gi Oh Card Image Background
IMAGE = pygame.image.load('yugioh_BACK.jpg').convert()
IMAGE = pygame.transform.scale(IMAGE, (150, 200))

"Testing of cards in hand"
BLUE_EYES = YuGiOhCardSprite('blue_eyes_card.jpg')
DARK_MAG = YuGiOhCardSprite('Dark_Magician.jpg')
EXODIA = YuGiOhCardSprite('exodia_card.png')
fake_trap_card = YuGiOhCardSprite('fake_trap_card.png')
jinzo = YuGiOhCardSprite('jinzo_card.png')
pot_of_greed = YuGiOhCardSprite('pot_of_creed.jpg')


WHITE = (255, 255, 255)
BLUE = (66, 138, 245)

#Opponent Top Row
DISPLAYSURF.blit(IMAGE, (30, 50))
DISPLAYSURF.blit(IMAGE, (230, 50))
DISPLAYSURF.blit(IMAGE, (430, 50))
DISPLAYSURF.blit(IMAGE, (630, 50))
DISPLAYSURF.blit(IMAGE, (830, 50))
DISPLAYSURF.blit(IMAGE, (1030, 50))

#Opponent Bottom Row

DISPLAYSURF.blit(IMAGE, (30, 50))
DISPLAYSURF.blit(IMAGE, (30, 270, 150, 200))
DISPLAYSURF.blit(IMAGE, (230, 270, 150, 200))
DISPLAYSURF.blit(IMAGE, (430, 270, 150, 200))
DISPLAYSURF.blit(IMAGE, (630, 270, 150, 200))
DISPLAYSURF.blit(IMAGE, (830, 270, 150, 200))
DISPLAYSURF.blit(IMAGE, (1030,270, 150, 200))

pygame.draw.line(DISPLAYSURF, BLUE, (30, 510), (1170, 510))

#Player Top Row
DISPLAYSURF.blit(IMAGE, (30, 550, 150, 200))
DISPLAYSURF.blit(IMAGE, (230,550, 150, 200))
DISPLAYSURF.blit(IMAGE, (430,550, 150, 200))
DISPLAYSURF.blit(IMAGE, (630,550, 150, 200))
DISPLAYSURF.blit(IMAGE, (830,550, 150, 200))
DISPLAYSURF.blit(IMAGE, (1030,550, 150, 200))

#Player Bottom Row
DISPLAYSURF.blit(IMAGE, (30, 770, 150, 200))
DISPLAYSURF.blit(IMAGE, (230,770, 150, 200))
DISPLAYSURF.blit(IMAGE, (430,770, 150, 200))
DISPLAYSURF.blit(IMAGE, (630,770, 150, 200))
DISPLAYSURF.blit(IMAGE, (830,770, 150, 200))
DISPLAYSURF.blit(IMAGE, (1030,770, 150, 200))

hand_group = pygame.sprite.Group()

while True:
    pygame.display.update()
    cursor_x , cursor_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if(cursor_x >= 300 and cursor_x <= 900):
        if(cursor_y >= 970 and cursor_y <= 999):
            print(show_hand)
            if show_hand is False:
                hand_group.add(BLUE_EYES, DARK_MAG, EXODIA, fake_trap_card,
                               jinzo, pot_of_greed)
                hand_group.update()
                hand_group.draw(DISPLAYSURF)
            show_hand = True
    else:
        hand_group.update()
        show_hand = False
            

    


        
