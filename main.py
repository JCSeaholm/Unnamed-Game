#pygame is the multimedia library
import pygame
#we'll need some math I'm sure
import numpy
#sys should make a few things like exiting smoother
import sys
#we should put settings in a different file just to keep everything clean
import settings as s

pygame.init()

class aight(object):
    pass

#Use pygame.FULLSCREEN for fullscreen
pygame.display.set_mode((s.userSetWidth, s.userSetWidth))

def changeWindowSize(width, height):
    s.setDimensions(width, height)
    pygame.display.set_mode((width, height))

def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()

#we don't need these, but they're there for safety
pygame.quit()
sys.exit()
