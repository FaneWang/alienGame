import sys
import pygame
from settings.settings import Settings
from ships.ship import Ship
# from utils.utils import *
from utils.utils import *

def runGame():
    # Initialize the game and create a screen object
    pygame.init()
    gameSettings = Settings()
    screen = pygame.display.set_mode((gameSettings.screenWidth,gameSettings.screenHeight))
    pygame.display.set_caption("Alien_Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        checkEvents(ship)
        ship.updateMoving()
        updateScreen(gameSettings,ship,screen)

runGame()


