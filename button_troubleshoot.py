import pygame
from constants import *

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))


# button class
class Button():

    def __init__(self, msg, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.topleft = (x, y)
        self.clicked = False
        self.font = pygame.font.SysFont("Georgia", 25, bold=True)
        self.surf = self.font.render(msg, True, "white")

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


# create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

# create button instances
start_button = Button("Hit", 30, 200, 150, 50)
exit_button = Button("Stand", 30, 300, 150, 50)

# game loop
run = True
while run:

    gameDisplay.blit(scaled_image, [0, 0])
    pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

    if start_button.draw():
        print('START')
    if exit_button.draw():
        print('EXIT')

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
