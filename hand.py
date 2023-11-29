"""
    hand.py
    creating the hand class
"""


class Hand:
    """ class: Hand
        Attributes: cards, value
        Methods: add_card (appends a new card to cards)
                 calc_value (calculates the value of the hand)
    """

    def __init__(self, cards=None, value=0):
        """
            Constructor -- creates a new instance of a hand
            Parameters: self -- the current object
                        cards -- a list of cards in the hand
                        value -- value of the hand
        """
        if cards is None:
            cards = []

        self.cards = cards
        self.value = value
