import copy
import random
import time
import webbrowser
import pygame
from constants import *
from hand import Hand
from deck import Deck
from button import Button
from test_xinui import visualize_cards
from unittest.mock import call
from unittest.mock import patch

clock = pygame.time.Clock()
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))


def test_visualize_cards():
    # Create a player and dealer with some cards
    player = Hand()
    player.add_card(2)
    player.add_card(3)
    dealer = Hand()
    dealer.add_card(11)
    dealer.add_card(10)

    # Set reveal to True to show both dealer's cards
    reveal = True

    # Call the visualize_cards function
    visualize_cards(player, dealer, reveal)

    # Assert that the cards are displayed correctly
    with patch("pygame.draw.rect") as mock_rect:
        # Run your test code here...

        # Then check the arguments that were passed to the mock:
        assert mock_rect.call_args_list == [
            call(gameDisplay, white, pygame.Rect(600, 450, 130, 190), 0, 5),
            call(gameDisplay, red, pygame.Rect(600, 450, 130, 190), 5, 5),
            call(gameDisplay, white, pygame.Rect(700, 450, 130, 190), 0, 5),
            call(gameDisplay, red, pygame.Rect(700, 450, 130, 190), 5, 5),
            call(gameDisplay, white, pygame.Rect(600, 150, 130, 190), 0, 5),
            call(gameDisplay, red, pygame.Rect(600, 150, 130, 190), 5, 5),
            call(gameDisplay, white, pygame.Rect(700, 150, 130, 190), 0, 5),
            call(gameDisplay, red, pygame.Rect(700, 150, 130, 190), 5, 5),
        ]
    with patch("pygame.draw.rect") as mock_rect:
        # Run your test code here...

        # Then check the arguments that were passed to the mock:
        assert mock_rect.call_args_list == [
            call(textfont.render("2", True, black), (610, 460)),
            call(textfont.render("3", True, black), (710, 460)),
            call(textfont.render("A", True, black), (610, 160)),
            call(textfont.render("??", True, black), (710, 160)),
        ]
    assert pygame.display.update.called


if __name__ == "__main__":
    test_visualize_cards()
    print("Everything passed")
