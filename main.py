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
#will later turn this into the base class for some polymorphism
class Player(object):
    def __init__(self):
        #loads an image onto an object,
        #convert is used for consistency between the display and the surface
        self.image = pygame.image.load("placeholder_player.png").convert()
        #pygame .get_rect() will create an object for us holding the rect coordinates of the image
        self.coord = self.image.get_rect()

        self.coord.x = 200
        self.coord.y = 200

        velocity = 1

    #function used to create movement for the player, kinda like a vector unit
    def movement(self, xDirect, yDirect):
        self.rect.x += xDirect*self.velocity
        self.rect.y += yDirect*self.velocity

def setup():
    player = Player()
    #probably will return more stuff later
    return player

def update(surfaces):
    pass

def changeWindowSize(width, height, gameWindow):
    #maybe add in stuff to check for aspect ratio
    s.setDimensions(width, height)
    gameWindow = pygame.display.set_mode((width, height))

def main( setup() ):
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
        with currentKey as pygame.key.get_pressed():
            if currentKey[pygame.K_RIGHT]:
                player.movement(1,0)
            if currentKey[pygame.K_LEFT]:
                player.movement(-1,0)
            if currentKey[pygame.K_UP]:
                player.movement(0,-1)
            if currentKey[pygame.K_DOWN]:
                player.movement(0,1)

        update(surface_to_update)
main()

#we don't need these, but they're there for safety
pygame.quit()
sys.exit()
