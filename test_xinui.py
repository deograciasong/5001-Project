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


def choose_bet():
    """
    displays a screen for the user to select which bet size they would like to choose
    parameters: None
    returns: bet (int)
    """

    # creating a button for the betting options
    button_5 = Button("$5", 30, 315, 150, 50)
    button_10 = Button("$10", 280, 315, 150, 50)
    button_25 = Button("$25", 530, 315, 150, 50)
    button_50 = Button("$50", 780, 315, 150, 50)
    button_100 = Button("$100", 1003, 315, 150, 50)
    button_reset = Button("Reset", 420, 500, 150, 50)
    button_bet = Button("Bet", 620, 500, 150, 50)

    bet = 0
    run = True
    while run:
        gameDisplay.blit(scaled_image, [0, 0])
        pygame.draw.rect(
            gameDisplay, black, pygame.Rect(0, 250, display_width, display_height / 4)
        )

        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

        # checking if a button was clicked and acting accordingly
        if button_5.check_click():
            bet += 5
        if button_10.check_click():
            bet += 10
        if button_25.check_click():
            bet += 25
        if button_50.check_click():
            bet += 50
        if button_100.check_click():
            bet += 100
        if button_reset.check_click():
            bet = 0
        if button_bet.check_click():
            run = False

        # draws the buttons
        button_5.draw()
        button_10.draw()
        button_25.draw()
        button_50.draw()
        button_100.draw()
        button_reset.draw()
        button_bet.draw()

        # visualize the current bet state
        pygame.draw.circle(gameDisplay, black, (600, 125), 90)
        surf = font_bet.render(f"${bet}", True, white)
        gameDisplay.blit(surf, (550, 95))

        pygame.display.update()
    return bet


def player_action(player, shoe, bet):
    """
    performs all actions requested by the player
    determines which button is clicked by user then acts accordingly
    parameters: player (object: Class Hand)
    returns: bet (int, value of the bet)
    """

    # creating the player action buttons
    hit_button = Button("Hit", 30, 200, 150, 50)
    stand_button = Button("Stand", 30, 300, 150, 50)
    double_button = Button("Double", 30, 400, 150, 50)

    run = True
    while run:
        gameDisplay.blit(scaled_image, [0, 0])
        pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

        # checking if the hit button was clicked and acting accordingly
        if hit_button.check_click():
            print("Hit")
            player.add_card(shoe.draw_card())
            player.calc_value()
            print(player)
            if player.get_value() > 21:
                run = False

        # checking if the stand button was clicked and acting accordingly
        if stand_button.check_click():
            run = False
            print("Stand")

        # checking if the double button was clicked and acting accordingly
        if double_button.check_click():
            print("Double")
            player.add_card(shoe.draw_card())
            player.calc_value()
            print(player)
            bet *= 2
            run = False

        # drawing the buttons
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
        grey, pygame.Rect(0, 0, display_width, display_height)
    )  # Clear a specific area of the display
    statistics_text = textfont.render(
        f"Rounds: {rounds} Wins: {wins} Losses: {losses} Pushes: {pushes}", True, black
    )
    gameDisplay.blit(statistics_text, (300, 300))
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
    bank = int(input("How much money are you willing to lose?" "(gamble responsibly!)"))

    pygame.display.set_caption("Pygame Blackjack!")
    gameDisplay.blit(scaled_image, [0, 0])
    pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

    while (shoe.get_remaining_cards() > cut_off) and run:
        # generate user input for bet
        bet = choose_bet()

        # create player hand (object)
        # create dealer hand (object)
        player = Hand(cards=[], value=0)
        dealer = Hand(cards=[], value=0)

        for i in range(2):
            player.add_card(shoe.draw_card())
            dealer.add_card(shoe.draw_card())

        player.calc_value()
        dealer.calc_value()

        # Display player's hand
        player_cards = player.cards
        for i, card in enumerate(player_cards):
            card_text = textfont.render(str(card), True, black)
            card_rect = pygame.Rect(600 + i * 100, 450 + i * 10, 130, 190)
            pygame.draw.rect(gameDisplay, white, card_rect, 0, 5)  # Draw a rectangle
            gameDisplay.blit(card_text, (card_rect.x + 10, card_rect.y + 10))
            pygame.draw.rect(
                gameDisplay, red, card_rect, 5, 5
            )  # Draw a rectangle with a border

        # Display dealer's hand
        dealer_cards = dealer.cards
        for i, card in enumerate(dealer_cards):
            card_text = textfont.render(str(card), True, black)
            card_rect = pygame.Rect(600 + i * 100, 150 + i * 10, 130, 190)
            pygame.draw.rect(gameDisplay, white, card_rect, 0, 5)  # Draw a rectangle
            gameDisplay.blit(card_text, (card_rect.x + 10, card_rect.y + 10))
            pygame.draw.rect(
                gameDisplay, red, card_rect, 5, 5
            )  # Draw a rectangle with a border

        pygame.display.update()

        # Display cards using Pygame GUI
        player_hand_text = textfont.render("Player's Hand: ", True, black)
        dealer_hand_text = textfont.render("Dealer's Hand: ", True, black)

        gameDisplay.blit(player_hand_text, (300, 450))
        gameDisplay.blit(dealer_hand_text, (300, 150))

        pygame.display.update()
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
        dealer_action(dealer, shoe)
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
