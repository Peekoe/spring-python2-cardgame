import pygame, sys
from pathlib import Path
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1920, 1080), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
unoCards = pygame.image.load('uno.png')
x = 10
y = 10
direction = 'right'
texture = Rect(0, 0, 400, 580)
button = Rect(0, 580, 400, 580)
showButton = True

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        x += 5
        if x == 280:
            direction = 'down'
    elif direction == 'down':
        y += 5
        if y == 220:
            direction = 'left'
    elif direction == 'left':
        x -= 5
        if x == 10:
            direction = 'up'
    elif direction == 'up':
        y -= 5
        if y == 10:
            direction = 'right'

    
    # card size for the second 2
    
    # x,y first 2

    DISPLAYSURF.blit(unoCards, (x, y), texture)
    if showButton:
        button.update(x, y, 400, 580)
    mouse = pygame.mouse.get_pos()
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        [unocards]
        if button.collidepoint(mouse) and event.type == MOUSEBUTTONDOWN:
            showButton = False
            print("clicked")
    pygame.display.update()
    fpsClock.tick(FPS)