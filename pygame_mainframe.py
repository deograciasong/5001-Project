import copy
import random
import pygame
from constants import *
from hand import Hand

pygame.init()

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))


###text object render
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def end_text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


# game text display
def game_texts(text, x, y):
    TextSurf, TextRect = text_objects(text, textfont)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def game_finish(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, game_end, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def black_jack(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, blackjack, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextRect)


def main():
    run = True
    decks = 8
    dict_card_value = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11,
    }

    dict_remaining_cards = {
        "2": 4 * decks,
        "3": 4 * decks,
        "4": 4 * decks,
        "5": 4 * decks,
        "6": 4 * decks,
        "7": 4 * decks,
        "8": 4 * decks,
        "9": 4 * decks,
        "10": 4 * decks,
        "J": 4 * decks,
        "Q": 4 * decks,
        "K": 4 * decks,
        "A": 4 * decks,
    }

    shoe = 52 * decks
    cut_off = shoe * 0.20

    screen = pygame.display.set_mode([display_width, display_height])
    pygame.display.set_caption("Pygame Blackjack!")
    gameDisplay.blit(scaled_image, [0, 0])
    pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

    while (shoe > cut_off) and run:
        # create player hand (object)
        # create dealer hand (object)
        # display both hands

        # create a loop for player action
        # generate user input to determine action
        # display new player hand

        # create loop for dealer action
        # hit until can no longer hit or bust
        # display new dealer hand

        # determine who won
        # calculate the remaining balance of the player

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            button("Deal", 30, 100, 150, 50, light_slat, dark_slat)
            button("Hit", 30, 200, 150, 50, light_slat, dark_slat)
            button("Stand", 30, 300, 150, 50, light_slat, dark_slat)
            button("Double", 30, 400, 150, 50, light_slat, dark_slat)
            # button("EXIT", 30, 600, 150, 50, red, dark_red)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
