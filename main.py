#pygame is the multimedia library
import pygame
#we'll need some math I'm sure
import numpy
#sys should make a few things like exiting smoother
import sys
#we should put settings in a different file just to keep everything clean
import settings as s

pygame.init()

#object to hold information about a player
class Player(object):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def changePosX(self, pos_x):
        self.pos_x = pos_x

    def changePosY(self, pos_y):
        self.pos_y = pos_y

def setup():
    pass

def update():
    pass

def changeWindowSize(width, height, gameWindow):
    #maybe add in stuff to check for aspect ratio
    s.setDimensions(width, height)
    gameWindow = pygame.display.set_mode((width, height))

def main():
    #Use pygame.FULLSCREEN for fullscreen
    #object for the window
    gameWindow = pygame.display.set_mode((s.userSetWidth, s.userSetWidth))
    #a list to hold the surfaces/rectangles that will need to be updated
    surface_to_update = []

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
