import copy
import random
import pygame
from constants import *
from hand import Hand
from deck import Deck

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

def start_menu():
    screen_width = display_width
    screen_height = display_height
    font = pygame.font.SysFont('Times New Roman', 35)
    title = font.render("BlackJack", True, (255, 255, 255))
    deal_text = font.render("Press Space to Deal", True, (255, 255, 255))
    exit_text = font.render("Press ESC to Exit", True, (255, 255, 255))
    gameDisplay.blit(title, (screen_width / 2 - title.get_width() / 2, screen_height / 2 - title.get_height() / 2))
    gameDisplay.blit(deal_text, (screen_width / 2 - deal_text.get_width() / 2, screen_height / 2 + deal_text.get_height() / 2))
    gameDisplay.blit(exit_text, (screen_width / 2 - exit_text.get_width() / 2, screen_height / 4 - exit_text.get_height() / 2))
    pygame.display.update()

def end_of_round_menu():
    screen_width = display_width
    screen_height = display_height
    font = pygame.font.SysFont('Times New Roman', 35)
    if bank > 0:
        title = font.render("You" + str(win_status) + "Press Space to Deal Again or Press ESC to Exit", True, (255, 255, 255))
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

    start_menu()

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
    #bank = int(input("How much money are you willing to lose?"
                     #"(gamble responsibly!)"))

    screen = pygame.display.set_mode([display_width, display_height])
    pygame.display.set_caption("Pygame Blackjack!")
    gameDisplay.blit(scaled_image, [0, 0])
    pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

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
            #win_status = "won"
            continue

        # determine who won
        # calculate the remaining balance of the player\
        if player.get_value < dealer.get_value:
            losses += 1
            bank -= bet
            rounds += 1
            #win_status = "won"
        elif player.get_value > dealer.get_value:
            wins += 1
            bank += bet
            rounds += 1
            #win_status = "lost"
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
