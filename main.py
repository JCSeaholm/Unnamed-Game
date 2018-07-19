#pygame is the multimedia library
import pygame
#we'll need some math I'm sure
import numpy
#sys should make a few things like exiting smoother
import sys
#we should put settings in a different file just to keep everything clean
import settings as s

pygame.init()

class Player(object):
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_x
    def changePosX(self):
        pass
    def changePosY(self):
        pass

def setup():
    pass

def changeWindowSize(width, height, gameWindow):
    #maybe add in stuff to check for aspect ratio
    s.setDimensions(width, height)
    gameWindow = pygame.display.set_mode((width, height))

def main():
    #Use pygame.FULLSCREEN for fullscreen
    gameWindow = pygame.display.set_mode((s.userSetWidth, s.userSetWidth))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #
main()

#we don't need these, but they're there for safety
pygame.quit()
sys.exit()
