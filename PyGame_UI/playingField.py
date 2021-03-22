import pygame
from pygame.locals import *

pygame.init()

show_hand = False
DISPLAYSURF = pygame.display.set_mode((1200,1000))

# Yu Gi Oh Card Image Background
IMAGE = pygame.image.load('yugioh_BACK.jpg').convert()
IMAGE = pygame.transform.scale(IMAGE, (150, 200))

"Testing of cards in hand"
BLUE_EYES = pygame.image.load('blue_eyes_card.jpg').convert()
BLUE_EYES = pygame.transform.scale(BLUE_EYES, (100, 150))

DARK_MAG = pygame.image.load('Dark_Magician.jpg').convert()
DARK_MAG = pygame.transform.scale(DARK_MAG, (100, 150))

EXODIA = pygame.image.load('exodia_card.png').convert()
EXODIA = pygame.transform.scale(EXODIA, (100, 150))

fake_trap_card = pygame.image.load('fake_trap_card.png').convert()
fake_trap_card = pygame.transform.scale(fake_trap_card, (100, 150))

jinzo = pygame.image.load('jinzo_card.png').convert()
jinzo = pygame.transform.scale(jinzo, (100, 150))

pot_of_greed = pygame.image.load('pot_of_creed.jpg').convert()
pot_of_greed = pygame.transform.scale(pot_of_greed, (100, 150))


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

"Hand Card Coordinates"
def showCards(card1, card2, card3, card4, card5, card6):
    DISPLAYSURF.blit(BLUE_EYES, card1)
    DISPLAYSURF.blit(DARK_MAG, card2)
    DISPLAYSURF.blit(EXODIA, card3)
    DISPLAYSURF.blit(fake_trap_card, card4)
    DISPLAYSURF.blit(jinzo, card5)
    DISPLAYSURF.blit(pot_of_greed, card6)



while True:
    pygame.display.update()
    DISPLAYSURF.copy()
    cursor_x , cursor_y = pygame.mouse.get_pos()
    card1 = (0, 1000)
    card2 = (0, 1000)
    card3 = (0, 1000)
    card4 = (0, 1000)
    card5 = (0, 1000)
    card6 = (0, 1000)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if(cursor_x >= 300 and cursor_x <= 900):
        if(cursor_y >= 970 and cursor_y <= 999):
            showCards((150, 850),(300, 850),(450, 850),
                      (600, 850),(750, 850),(900, 850))

    

