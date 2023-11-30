import copy
import random
import pygame
from hand import Hand

pygame.init()

def main():
    run = True
    decks = 8
    dict_card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
                       "Q": 10, "K": 10, "A": 11}

    dict_remaining_cards = {"2": 4 * decks, "3": 4 * decks, "4": 4 * decks,
                            "5": 4 * decks, "6": 4 * decks, "7": 4 * decks,
                            "8": 4 * decks, "9": 4 * decks, "10": 4 * decks,
                            "J": 4 * decks, "Q": 4 * decks, "K": 4 * decks,
                            "A": 4 * decks}

    shoe = 52 * decks
    cut_off = shoe * .20

    WIDTH = 600
    HEIGHT = 900
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('Pygame Blackjack!')

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
        """
        # display both hands

        # create a loop for player action
            # generate user input to determine action
            # display new player hand


        # create loop for dealer action
            # hit until can no longer hit or bust
            # display new dealer hand

        # determine who won
        # calculate the remaining balance of the player
        if player.get_value > dealer.get_value:
            wins += 1
            bank += bet
            rounds += 1
        elif player.get_value < dealer.get_value:
            losses += 1
            bank -= bet
            rounds += 1
        else:
            pushes += 1
            rounds += 1

        # update statistics and visualize


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
