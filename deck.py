"""
    deck.py
    creating the hand class
"""
decks = 8
dict_remaining_cards = {"2": 4 * decks, "3": 4 * decks, "4": 4 * decks,
                        "5": 4 * decks, "6": 4 * decks, "7": 4 * decks,
                        "8": 4 * decks, "9": 4 * decks, "10": 4 * decks,
                        "J": 4 * decks, "Q": 4 * decks, "K": 4 * decks,
                        "A": 4 * decks}

class Deck:
    """ class: Deck
        Attributes: remaining_cards, drawn_count
        Methods: draw_card (removes card from deck)
                 shuffle
                 remaining_count
    """
    def __init__(self, remaining_cards=dict_remaining_cards, drawn_count=0):
        """
            Constructor -- creates a new instance of a hand
            Parameters: self -- the current object
                        card -- card that is drawn
                        drawn_count -- number of cards that have been drawn
        """
        self.remaining_cards = remaining_cards
        self.drawn_count = drawn_count
    def draw_card(self):
        import random
        options = []


    def shuffle(self):
        # creating full 52*8 deck again
    def remaining_count(self):