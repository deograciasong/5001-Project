import copy
import random
import pygame
from constants import *
from hand import Hand
from deck import Deck
import time

pygame.init()

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))


def start_menu():
    gameDisplay.fill((0, 0, 0))
    run = True
    # while run is true show the start menu screen
    while run == True:
        title = font_startmenu.render("BlackJack", True, (255, 255, 255))
        deal_text = font_startmenu.render("Press Space to Deal", True, (255, 255, 255))
        instruction_text = font_startmenu.render("Press i for instructions", True, (255, 255, 255))
        exit_text = font_startmenu.render("Press ESC to Exit", True, (255, 255, 255))
        gameDisplay.blit(title, (display_width / 2 - title.get_width() / 2, display_height / 2 - title.get_height() / 2))
        gameDisplay.blit(deal_text,
                         (display_width / 2 - deal_text.get_width() / 2, display_height / 2 + deal_text.get_height() / 2))
        gameDisplay.blit(exit_text,
                         (display_width / 2 - exit_text.get_width() / 2, display_height / 4 + exit_text.get_height() / 2))
        gameDisplay.blit(instruction_text,
                         (display_width / 2 - instruction_text.get_width() / 2, display_height / 6 + instruction_text.get_height() / 2))
        pygame.display.update()
        # checking which keys are pressed by players
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                # if escape key is pressed quit game
                if event.key == pygame.K_ESCAPE:
                    run = False
                # if i is pressed change to the instruction screen
                elif event.key == pygame.K_i:
                    instruction()
                # if d is pressed continue on the main function
                elif event.key == pygame.K_SPACE:
                    return True
    return run



def instruction():
    gameDisplay.fill((0, 0, 0))
    run = True
    while run:
        font = pygame.font.SysFont('Times New Roman', 30)
        title = font.render("Instructions (press r to return to the start menu)", True, (255, 255, 255))
        instruction_text = font.render("The Pack\n The standard 52-card pack is used, "
                                       "but in most casinos several decks of cards are shuffled together. "
                                       "The six-deck game (312 cards) is the most popular. "
                                       "In addition, the dealer uses a blank plastic card, which is never dealt,"
                                       "but is placed toward the bottom of the pack to indicate when it "
                                       "will be time for the cards to be reshuffled. When four or more decks are used, "
                                       "they are dealt from a shoe (a box that allows the dealer to remove "
                                       "cards one at a time, face down, without actually holding one or more packs).\n"
                                       "Object of the Game\n", True, (255, 255, 255))
        gameDisplay.blit(title, (display_width / 2 - title.get_width() / 2, display_height / 2 - title.get_height() / 2))
        gameDisplay.blit(instruction_text,
                         (display_width / 2 - instruction_text.get_width() / 2, display_height / 2 + instruction_text.get_height() / 2))
        pygame.display.update()

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                # if escape key is pressed quit game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                # if r is pressed continue on the main function
                elif event.key == pygame.K_r:
                    start_menu()


def end_of_round_menu():
    screen_width = display_width
    screen_height = display_height
    font = pygame.font.SysFont('Times New Roman', 35)
    if bank > 0:
        title = font.render("You" + str(win_status) + "Press Space to Deal Again or Press ESC to Exit", True,
                            (255, 255, 255))
    elif bank <= 0:
        title = font.render("Game Over Press ESC to Exit", True, (255, 255, 255))
    gameDisplay.blit(title, (screen_width / 2 - title.get_width() / 2, screen_height / 2 - title.get_height() / 2))
    pygame.display.update()

def main():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

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
    # bank = int(input("How much money are you willing to lose?"
    # "(gamble responsibly!)"))

    screen = pygame.display.set_mode([display_width, display_height])
    pygame.display.set_caption("Pygame Blackjack!")
    gameDisplay.blit(scaled_image, [0, 0])
    pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

    run = start_menu()

    while (shoe > cut_off) and run:
        # generate user input for bet
        bet = int(input("what is your bet size for the round?"))
        # create player hand (object)
        # create dealer hand (object)
        """
        player = Hand()
        dealer = Hand()

        for i in range(2):
            player.add_card(deck.draw_card)
            dealer.add_card(deck.draw_card)

        player.calc_value()
        dealer.calc_value()
        """

        # display both hands

        # create a loop for player action
        # generate user input to determine action
        # display new player hand
        if player.get_value > 21:
            losses += 1
            bank -= bet
            rounds += 1
            win_status = "lost"
            continue

        # create loop for dealer action
        # hit until can no longer hit or bust
        # display new dealer hand
        if dealer.get_value > 21:
            wins += 1
            bank += bet
            rounds += 1
            # win_status = "won"
            continue

        # determine who won
        # calculate the remaining balance of the player\
        if player.get_value < dealer.get_value:
            losses += 1
            bank -= bet
            rounds += 1
            # win_status = "won"
        elif player.get_value > dealer.get_value:
            wins += 1
            bank += bet
            rounds += 1
            # win_status = "lost"
        else:
            pushes += 1
            rounds += 1

        # update statistics and visualize

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            button("Deal", 30, 100, 150, 50, light_slat, dark_slat)
            button("Hit", 30, 200, 150, 50, light_slat, dark_slat)
            button("Stand", 30, 300, 150, 50, light_slat, dark_slat)
            button("Double", 30, 400, 150, 50, light_slat, dark_slat)
            # button("EXIT", 30, 600, 150, 50, red, dark_red)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
