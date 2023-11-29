"""
    hand.py
    creating the hand class
"""


CARD_VALUE = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
              "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
              "Q": 10, "K": 10, "A": 11}

class Hand:
    """ class: Hand
        Attributes: cards, value
        Methods: add_card (appends a new card to cards)
                 calc_value (calculates the value of the hand)
    """

    def __init__(self, cards=[], value=0):
        """
            Constructor -- creates a new instance of a hand
            Parameters: self -- the current object
                        cards -- a list of cards in the hand
                        value -- value of the hand
        """

        self.cards = cards
        self.value = value


    def add_card(self, card):
        self.cards.append(card)

    def calc_value(self):
        """
        calculates the value of the current hand and updates the
        value of the hand
        :return: None
        """
        value = 0
        for card in self.cards:
            value += CARD_VALUE[card]
            # checking if the card is an Ace and updating the value
            if card == 'A' and value > 21:
                value -= 10
        self.value = value

