import copy
import random
import time

import pygame
from constants import *
from hand import Hand
from deck import Deck
from button import Button

clock = pygame.time.Clock()
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))


def player_action(player, shoe, bet):
    """
    performs all actions requested by the player
    determines which button is clicked by user then acts accordingly
    parameters: player (object: Class Hand)
    returns: bet (int, value of the bet)
    """
    hit_button = Button("Hit", 30, 200, 150, 50, surf_hit)
    stand_button = Button("Stand", 30, 300, 150, 50, surf_stand)
    double_button = Button("Double", 30, 400, 150, 50, surf_double)
    hit_button.clicked = False

    run = True
    while run:
        gameDisplay.blit(scaled_image, [0, 0])
        pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

        if hit_button.check_click():
            print('Hit')
            player.add_card(shoe.draw_card())
            player.calc_value()
            print(player)
            if player.get_value() > 21:

                run = False

        if stand_button.check_click():
            run = False
            print('Stand')

        if double_button.check_click():
            print("Double")
            player.add_card(shoe.draw_card())
            player.calc_value()
            print(player)
            bet *= 2
            run = False

        hit_button.draw()
        stand_button.draw()
        double_button.draw()

        pygame.display.update()
    return bet


def dealer_action(dealer, shoe):
    """
    performs all actions of a dealer once the player action is over
    draws cards until the dealer's card values are over 16
    """
    while dealer.get_value() < 16:
        dealer.add_card(shoe.draw_card)
        dealer.calc_value()


def update_display(rounds, wins, losses, pushes):
    # update statistics and visualize
    gameDisplay.fill(
        grey, pygame.Rect(200, 600, display_width, display_height)
    )  # Clear a specific area of the display
    statistics_text = textfont.render(
        f"Rounds: {rounds} Wins: {wins} Losses: {losses} Pushes: {pushes}",
        True, black)
    gameDisplay.blit(statistics_text, (250, 600))
    pygame.display.update()
    time.sleep(1)


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

    pygame.display.set_caption("Pygame Blackjack!")
    gameDisplay.blit(scaled_image, [0, 0])
    pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

    while (shoe.get_remaining_cards() > cut_off) and run:
        # generate user input for bet
        bet = 1

        # create player hand (object)
        # create dealer hand (object)
        player = Hand(cards=[], value=0)
        dealer = Hand(cards=[], value=0)

        for i in range(2):
            player.add_card(shoe.draw_card())
            dealer.add_card(shoe.draw_card())

        player.calc_value()
        dealer.calc_value()

        # display both hands

        # create a loop for player action
        # generate user input to determine action
        # display new player hand
        print(player)
        bet = player_action(player, shoe, bet)
        if player.get_value() > 21:
            losses += 1
            bank -= bet
            rounds += 1
            update_display(rounds, wins, losses, pushes)
            continue

        # create loop for dealer action
        # hit until can no longer hit or bust
        # display new dealer hand
        if dealer.get_value() > 21:
            wins += 1
            bank += bet
            rounds += 1
            update_display(rounds, wins, losses, pushes)
            continue

        # determine who won
        # calculate the remaining balance of the player
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

        update_display(rounds, wins, losses, pushes)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
