import copy
import random
import pygame

pygame.init()

decks = 8
dict_card_value = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6,
                    "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10,
                    "Q" : 10, "K" : 10, "A" : 11}

dict_remaining_cards = {"2" : 4 * decks, "3" : 4 * decks, "4" : 4 * decks,
                       "5" : 4 * decks, "6" : 4 * decks, "7" : 4 * decks,
                       "8" : 4 * decks, "9" : 4 * decks, "10" : 4 * decks,
                       "J" : 4 * decks, "Q" : 4 * decks, "K" : 4 * decks,
                       "A" : 4 * decks}

shoe = 52 * decks
cut_off = shoe * .20

WIDTH = 600
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Blackjack!')

while shoe > cut_off:
    # call blackgame (dict_remaining_cards, shoe)
    # returns 

