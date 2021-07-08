import random

from game.card import Card, CardValue, Suit

class Deck():
    """This class represents a deck of cards. The cards may be drawn from. Cards can only be taken, never put back
    """    

    def __init__(self):
        """Creates a deck of 52 cards. Does not shuffle it
        """        
        
        self.__createDeck()

    def shuffle(self):
        """Shuffles the deck of cards
        """        
        random.shuffle(self.cards)

    def drawCard(self) -> Card:
        """Removes a card from the deck and returns it

        Returns:
            Card: A card from the deck
        """        
        card = self.cards.pop()
        return card

    def isEmpty(self) -> bool:
        """checks if the deck is empty

        Returns:
            bool: returns true if deck is empty, otherwise false
        """        
        return len(self.cards) == 0

    def __createDeck(self):
        """Initializes the deck with 52 cards
        """        
        self.cards = []
        for i in CardValue:
            for c in Suit:
                self.cards.append(Card(i, c))