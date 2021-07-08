from enum import IntEnum

class Card:
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.number.value) + "_" + str(Suit.str(self.suit))

    def __lt__(self, other):
        if (self.number == other.number):
            return self.suit < other.suit
        return self.number < other.number

    def __eq__(self, other):
        return self.number == other.number and self.suit == other.suit

class Suit(IntEnum):
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLOVERS = 4

    def str(suit) -> str:
        if suit == Suit.HEARTS:
            return "H"
        if suit == Suit.DIAMONDS:
            return "D"
        if suit == Suit.SPADES:
            return "S"
        if suit == Suit.CLOVERS:
            return "C"
        return "?"

class CardValue(IntEnum):
    ACE = 14
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13