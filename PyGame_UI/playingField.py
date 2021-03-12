import pygame
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1200,1000))

# Yu Gi Oh Card Image Background
IMAGE = pygame.image.load('yugioh_BACK.jpg').convert()
IMAGE = pygame.transform.scale(IMAGE, (150, 200))

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

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSec.tick(FPS)
        
