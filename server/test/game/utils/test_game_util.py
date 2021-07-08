from game.player import Player
import unittest

from game.card import *
from game.utils.game_util import GameUtil

class Test_GameUtil(unittest.TestCase):

    def test_moveIsAllSameTypeOfCard_SingleCard(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        move = [c1]
        self.assertTrue(GameUtil.moveIsAllSameTypeOfCard(move))

    def test_moveIsAllSameTypeOfCard_MultiCardDiff(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.TWO, Suit.HEARTS)
        move = [c1, c2]
        self.assertFalse(GameUtil.moveIsAllSameTypeOfCard(move))

    def test_moveIsAllSameTypeOfCard_MultiCardSame(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.ACE, Suit.DIAMONDS)
        move = [c1, c2]
        self.assertTrue(GameUtil.moveIsAllSameTypeOfCard(move))

    def test_playerHasCard_SingleCardMove_HasCard(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        move = [c1]
        playerHand = [c1]

        self.assertTrue(GameUtil.playerHasCards(playerHand, move))
    
    def test_playerHasCard_SingleCardMove_NotHasCard(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.TWO, Suit.HEARTS)
        move = [c2]
        playerHand = [c1]

        self.assertFalse(GameUtil.playerHasCards(playerHand, move))

    def test_playerHasCard_MultiCardMove_HasCards(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.ACE, Suit.DIAMONDS)
        c3 = Card(CardValue.ACE, Suit.SPADES)
        c4 = Card(CardValue.ACE, Suit.CLOVERS)
        move = [c1, c2, c3, c4]
        playerHand = [c1, c2, c3, c4]

        self.assertTrue(GameUtil.playerHasCards(playerHand, move))

    def test_playerHasCard_MultiCardMove_NotHasCards(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.ACE, Suit.DIAMONDS)
        c3 = Card(CardValue.ACE, Suit.SPADES)
        c4 = Card(CardValue.ACE, Suit.CLOVERS)
        move = [c1, c2, c3, c4]
        playerHand = [c1, c2, c3]

        self.assertFalse(GameUtil.playerHasCards(playerHand, move))

    def test_isValidMove_NoMove(self):
        playerHand = []
        self.assertFalse(GameUtil.isValidMove([], [], []))

    def test_isValidMove_NoLastMove(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        playerHand = [c1]
        move = [c1]
        self.assertTrue(GameUtil.isValidMove(playerHand, move, []))

    def test_isValidMove_MoveHasLessThanLastMove(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.ACE, Suit.DIAMONDS)
        c3 = Card(CardValue.ACE, Suit.SPADES)

        playerHand = [c1]
        move = [c1]
        lastMove = [c2, c3]

        self.assertFalse(GameUtil.isValidMove(playerHand, move, lastMove))

    def test_isValidMove_MoveIsLowerValue(self):
        c1 = Card(CardValue.TWO, Suit.HEARTS)
        c2 = Card(CardValue.ACE, Suit.DIAMONDS)
        
        playerHand = [c1]
        move = [c1]
        lastMove = [c2]

        self.assertFalse(GameUtil.isValidMove(playerHand, move, lastMove))

    def test_isValidMove_MoveIsLowerValue(self):
        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.TWO, Suit.DIAMONDS)
        
        playerHand = [c1]
        move = [c1]
        lastMove = [c2]

        self.assertTrue(GameUtil.isValidMove(playerHand, move, lastMove))