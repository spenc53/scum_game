import unittest
from game.card import Card, CardValue, Suit

class Test_Card(unittest.TestCase):

    def test_init(self):
        card = Card(CardValue.ACE, Suit.SPADES)
        self.assertEqual(card.number, CardValue.ACE)
        self.assertEqual(card.suit, Suit.SPADES)

    def test_sort(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.TWO, Suit.HEARTS)
        c3 = Card(CardValue.THREE, Suit.HEARTS)
        c4 = Card(CardValue.FOUR, Suit.HEARTS) 

        hand = [c2, c1, c4, c3]
        sorted_hand = [c2, c3, c4, c1]
        hand.sort()
        self.assertEqual(len(hand), 4)
        self.assertEqual(hand, sorted_hand)