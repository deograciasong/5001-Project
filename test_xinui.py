import copy
import random
import pygame
import time
from time import sleep
from constants import *
from hand import Hand
from deck import Deck

pygame.init()

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))


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
    text_x = button.x + (w - surf.get_width()) // 2  # Calculate the x-coordinate for center alignment
    text_y = button.y + (h - surf.get_height()) // 2  # Calculate the y-coordinate for center alignment
    gameDisplay.blit(surf, (text_x, text_y))
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
                print("bust")
            time.sleep(0.1)  # Add a small delay to reduce lag

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


def main():
    run = True
    decks = 8

    shoe = 52 * decks
    cut_off = shoe * 0.20

    # initialize a deck class here
    shoe = Deck()

    # initialize stats
    wins = 0
    losses = 0
    pushes = 0
    rounds = 0

    # initialize bankroll
    bank = int(input("How much money are you willing to lose?" "(gamble responsibly!)"))

    screen = pygame.display.set_mode([display_width, display_height])
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

        print(player)

        # ...

        # Display player's hand
        player_cards = player.get_cards()
        for i, card in enumerate(player_cards):
            card_text = textfont.render(str(card), True, black)
            card_rect = pygame.Rect(30 + i * 50, 600, 40, 60)
            pygame.draw.rect(gameDisplay, white, card_rect)
            gameDisplay.blit(card_text, (card_rect.x + 10, card_rect.y + 10))

        # Display dealer's hand
        dealer_cards = dealer.get_cards()
        for i, card in enumerate(dealer_cards):
            card_text = textfont.render(str(card), True, black)
            card_rect = pygame.Rect(30 + i * 50, 660, 40, 60)
            pygame.draw.rect(gameDisplay, white, card_rect)
            gameDisplay.blit(card_text, (card_rect.x + 10, card_rect.y + 10))

        pygame.display.update()
        print("Player's Hand:", player)
        print("Dealer's Hand:", dealer)

        # Display cards using Pygame GUI
        player_hand_text = textfont.render(f"Player's Hand: {player}", True, black)
        dealer_hand_text = textfont.render(f"Dealer's Hand: {dealer}", True, black)

        gameDisplay.blit(player_hand_text, (30, 500))
        gameDisplay.blit(dealer_hand_text, (30, 550))

        pygame.display.update()

        # create a loop for player action
        # generate user input to determine action
        # display new player hand
        bet = player_action(player, shoe, bet)
        print(player)
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    main()
