#pygame is the multimedia library
import pygame
#we'll need some math I'm sure
import numpy
#sys should make a few things like exiting smoother
import sys
#we should put settings in a different file just to keep everything clean
import settings as s

pygame.init()

"""classes"""

class aight(object):
    pass

"""functions and variables"""


def changeWindowSize(width, height):
    s.setWidth(width)
    s.setHeight(height)
    pygame.display.set_mode((width, height))

"""main"""

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
