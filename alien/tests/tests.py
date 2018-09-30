# import os 
# import sys
# print(os.getcwd())
# sys.path.append(os.getcwd())
from alien.settings.settings import Settings

def test():
    gameSettings = Settings()
    print(gameSettings.screenHeight)