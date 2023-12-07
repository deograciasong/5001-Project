import pygame
from constants import *

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))

class Button():

    def __init__(self,msg, x, y, width, height, surface):
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.topleft = (x, y)
        self.clicked = False
        self.surf = surface


    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        gameDisplay.blit(self.surf, (self.rect.x, self.rect.y))

        return action