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
        self.image = pygame.transform.scale(pygame.image.load("placeholder_player.png").convert(), (100, 100))
        #pygame .get_rect() will create an object for us holding the rect coordinates of the image
        self.coord = self.image.get_rect()

        self.coord.x = 200
        self.coord.y = 200

        #variables to hold the values for velocity and acceleration
        self.velocity_x = 1
        self.velocity_y = .5
        #the max that the postx and posty can reach
        self.max_momentum = 3
        #amt that the acceleration changes by per key event
        self.accel_change = .01

        #holds the amt of acceleration to be added to a movement
        self.postx = 0
        self.posty = 0

        self.moved = False

    #function used to create movement for the player, kinda like a vector unit
    def move(self, xDirect, yDirect):
        self.moved = True

        if self.postx > self.max_momentum:
            self.postx = self.max_momentum
        elif self.postx < -self.max_momentum:
            self.postx = -self.max_momentum

        if self.posty > self.max_momentum:
            self.posty = self.max_momentum
        elif self.posty < -self.max_momentum:
            self.posty = -self.max_momentum

        self.coord.x += xDirect*self.velocity_x + (self.postx*abs(self.postx))
        self.coord.y += yDirect*self.velocity_y + (self.posty*abs(self.posty))
        self.postx += self.accel_change*(xDirect)
        self.posty += self.accel_change*(yDirect)

    def movement(self, currentKey):
        self.moved = False

        if currentKey[pygame.K_RIGHT]:
            self.move(1, 0)
        if currentKey[pygame.K_LEFT]:
            self.move(-1, 0)
        if currentKey[pygame.K_UP]:
            self.move(0, -1)
        if currentKey[pygame.K_DOWN]:
            self.move(0, 1)

        if self.moved == False:
            self.move(0,0)

            #while the player doesn't hold any key, acceleration approaches 0
            if self.postx < 0:
                self.postx += self.accel_change
            elif self.postx > 0:
                self.postx -= self.accel_change

            if self.posty < 0:
                self.posty += self.accel_change
            elif self.posty > 0:
                self.posty -= self.accel_change

def setup():
    pass

def update(surfaces):
    pass

def changeWindowSize(width, height, gameWindow):
    #maybe add in stuff to check for aspect ratio
    s.setDimensions(width, height)
    gameWindow = pygame.display.set_mode((width, height))


#Use pygame.FULLSCREEN for fullscreen
#object for the window
gameWindow = pygame.display.set_mode((s.userSetWidth, s.userSetWidth))
entities_to_update = []
player = Player()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #sends key pressed object or dict (idk) to the movement function which handles the player movement
    #turned movement into a method so it can be used possibly with an array of Player base objects
    player.movement(pygame.key.get_pressed());


    #will want to use different technique to update the screen, this is too slow
    gameWindow.blit(player.image, (player.coord.x, player.coord.y))
    pygame.display.update()

#we don't need these, but they're there for safety
#there are some errors whenever you exit the window, maybe it's these
pygame.quit()
#sys.exit()
