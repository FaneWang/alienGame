import sys
import pygame

def checkEvents(ship):
    # Monitor the keyboard event and the mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = True
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = False
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = False

def updateScreen(gameSettings,ship,screen):
    screen.fill(gameSettings.bgColor)
    ship.blitMe()
    pygame.display.flip()