"""
    hand.py
    creating the hand class
"""

class Hand:
    ''' class: Hand
        Attributes: cards, value
        Methods: add_card (appends a new card to cards)
                 calc_value (calculates the value of the hand)
    '''


    def __init__(self, cards, value):
        self.cards = cards
        self.value = value
