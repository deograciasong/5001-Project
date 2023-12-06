import copy
import random
import pygame
from constants import *
from hand import Hand
from deck import Deck

pygame.init()

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))

'''
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
'''


def buttons(msg, x, y, w, h, ic, ac):
    font = pygame.font.SysFont("Georgia", 25, bold=True)
    surf = font.render(msg, True, "white")
    button = pygame.Rect(x, y, w, h)

    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                return msg
    a, b = pygame.mouse.get_pos()
    if button.x <= a <= button.x + w and button.y <= b <= button.y + h:
        pygame.draw.rect(gameDisplay, ac, button)
    else:
        pygame.draw.rect(gameDisplay, ic, button)
    gameDisplay.blit(surf, (button.x + 50, button.y + 5))
    pygame.display.update()


def player_action(player, shoe, bet):
    """
    performs all actions requested by the player
    determines which button is clicked by user then acts accordingly
    parameters: player (object: Class Hand)
    returns: bet (int, value of the bet)
    """
    run = True
    while run:
        hit = buttons("Hit", 30, 200, 150, 50, light_slat, dark_slat)
        if hit == "Hit":
            player.add_card(shoe.draw_card())
            player.calc_value()
            if player.get_value() > 21:
                run = False
            print("success")

        stand = buttons("Stand", 30, 300, 150, 50, light_slat, dark_slat)
        if stand == "Stand":
            run = False
            print("stand")

        double = buttons("Double", 30, 400, 150, 50, light_slat, dark_slat)
        if double == "Double":
            player.add_card(shoe.draw_card())
            player.calc_value()
            bet *= 2
            run = False
            print("double")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    return bet


def dealer_action(dealer, shoe):
    """
    performs all actions of a dealer once the player action is over
    draws cards until the dealer's card values are over 16
    """
    while dealer.calc_value() < 16:
        dealer.add_card(shoe.draw_card)


def main():
    run = True
    decks = 8
    cut_off = 52 * decks * 0.20

    # initialize a deck class here
    shoe = Deck()

    # initialize stats
    wins = 0
    losses = 0
    pushes = 0
    rounds = 0

    # initialize bankroll
    bank = int(input("How much money are you willing to lose?"
                     "(gamble responsibly!)"))

    screen = pygame.display.set_mode([display_width, display_height])
    pygame.display.set_caption("Pygame Blackjack!")
    gameDisplay.blit(scaled_image, [0, 0])
    pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

    while (shoe.get_remaining_cards() > cut_off) and run:
        # generate user input for bet
        bet = 1

        # create player hand (object)
        # create dealer hand (object)
        player = Hand(cards=[], value=0, cards_value=[])
        dealer = Hand(cards=[], value=0, cards_value=[])

        for i in range(2):
            player.add_card(shoe.draw_card())
            dealer.add_card(shoe.draw_card())

        player.calc_value()
        dealer.calc_value()

        # display both hands

        # create a loop for player action
        # generate user input to determine action
        # display new player hand
        bet = player_action(player, shoe, bet)
        if player.get_value() > 21:
            losses += 1
            bank -= bet
            rounds += 1
            continue

        # create loop for dealer action
        # hit until can no longer hit or bust
        # display new dealer hand
        if dealer.get_value() > 21:
            wins += 1
            bank += bet
            rounds += 1
            continue

        # determine who won
        # calculate the remaining balance of the player\
        if player.get_value() < dealer.get_value():
            losses += 1
            bank -= bet
            rounds += 1
        elif player.get_value() > dealer.get_value():
            wins += 1
            bank += bet
            rounds += 1
        else:
            pushes += 1
            rounds += 1

        # update statistics and visualize
        gameDisplay.fill(
            grey, pygame.Rect(200, 600, display_width, display_height)
        )  # Clear a specific area of the display
        statistics_text = textfont.render(
            f"Rounds: {rounds} Wins: {wins} Losses: {losses} Pushes: {pushes}",
            True,
            black,
        )
        gameDisplay.blit(statistics_text, (250, 600))

    pygame.quit()


if __name__ == "__main__":
    main()
