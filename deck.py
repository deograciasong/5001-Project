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
                        get_drawn_count -- number of cards that have been drawn
                        get_remaining_count -- number of cards left in the deck
        """
        self.remaining_cards = remaining_cards
        self.drawn_count = drawn_count

    def draw_card(self):
        import random
        # card, card_count = random.choice(self.remaining_cards)
        card = random.choice(list(self.remaining_cards.keys()))
        card_count = self.remaining_cards[card]
        while card_count == 0:
            # card, card_count = random.choice(self.remaining_cards)
            card = random.choice(list(self.remaining_cards.keys()))
            card_count = self.remaining_cards[card]
        self.remaining_cards[card] -= 1
        self.drawn_count += 1
        print(card)
        return card

    def shuffle(self):
        # creating full 52*8 deck again
        self.remaining_cards = dict_remaining_cards

    def get_drawn_count(self):
        return self.drawn_count

    def get_remaining_cards(self):
        return (52 * decks) - self.drawn_count
