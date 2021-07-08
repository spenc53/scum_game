
import unittest
import random

from game.deck import Deck

class Test_Deck(unittest.TestCase):

    def test_deckInitialize(self):
        d = Deck()
        self.assertEqual(len(d.cards), 52, "The deck does not have exactly 52 cards")

    def test_shuffle(self):
        d = Deck()
        c = d.cards[0]
        self.assertEqual(c, d.cards[0], "The first card not equal to itself")
        random.seed(42)
        d.shuffle()
        self.assertNotEqual(c, d.cards[0], "The deck is not shuffled")

    def test_draw(self):
        d = Deck()
        self.assertIsNotNone(d.drawCard())
        self.assertEqual(len(d.cards), 51)

    def test_isEmpty(self):
        d = Deck()
        for _ in range(52):
            self.assertFalse(d.isEmpty())
            d.drawCard()
        self.assertTrue(d.isEmpty())

if __name__ == '__main__':
    unittest.main()