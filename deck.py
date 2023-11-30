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
        Attributes:
        Methods: draw_card (removes card from deck)
                 shuffle
                 remaining_count
    """
    #hi