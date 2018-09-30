import pygame
import os

class Ship():
    def __init__(self,screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\images\ship.bmp")
        self.imageRect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        # Put each new ship at the bottom center of the screen
        self.imageRect.centerx = self.screenRect.centerx
        self.imageRect.bottom = self.screenRect.bottom

        # Movement flags
        self.movingRight = False
        self.movingLeft = False

    def blitMe(self):
        """Draw the ship at the designated position"""
        self.screen.blit(self.image,self.imageRect)

    def updateMoving(self):
        """Move the ship according to the Movement flags"""
        if self.movingRight and self.imageRect.right < self.screenRect.right:
            self.imageRect.centerx += 1
        if self.movingLeft and self.imageRect.left > self.screenRect.left:
            self.imageRect.centerx -= 1

if __name__ == "__main__":
    # BASE_DIR = 
    # print("A stupid pig")

    # __file__,如果当前文件在sys.path,那么返回相对路径，如果不在，返回绝对路径
    print(__file__)
    # os.path.abspath返回文件的绝对路径，无视平台
    print(os.path.abspath(__file__)) 
    # #os.path.dirname返回文件的上级目录，无视平台
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\images\ship.bmp")
