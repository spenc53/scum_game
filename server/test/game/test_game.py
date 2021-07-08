import unittest

from game.game import Game, GameState, TradingValue
from game.game_info import GameInfo
from game.player import Player
from game.card import *

class Test_Game(unittest.TestCase):

    def test_gameInit_TwoPlayers(self):
        gameInfo = GameInfo("test_game", "1234", 2)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")

        game = Game(gameInfo)

        self.assertTrue("1" in game.order)
        self.assertTrue("2" in game.order)

        self.assertTrue("1" in game.playersHands)
        self.assertTrue("2" in game.playersHands)

        self.assertEqual(len(game.playersHands["1"]), 26)
        self.assertEqual(len(game.playersHands["2"]), 26)

        self.assertEqual(game.trading["1"]["dstPlayer"], "2")
        self.assertEqual(game.trading["1"]["amount"], 2)
        self.assertEqual(game.trading["1"]["tradeValue"], TradingValue.ANY)

        self.assertEqual(game.trading["2"]["dstPlayer"], "1")
        self.assertEqual(game.trading["2"]["amount"], 2)
        self.assertEqual(game.trading["2"]["tradeValue"], TradingValue.BEST)

    def test_gameInit_FourPlayers(self):
        gameInfo = GameInfo("test_game", "1234", 6)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")
        gameInfo.addPlayer("3")
        gameInfo.addPlayer("4")

        game = Game(gameInfo)

        self.assertTrue("1" in game.order)
        self.assertTrue("2" in game.order)
        self.assertTrue("3" in game.order)
        self.assertTrue("4" in game.order)

        self.assertTrue("1" in game.playersHands)
        self.assertTrue("2" in game.playersHands)
        self.assertTrue("3" in game.playersHands)
        self.assertTrue("4" in game.playersHands)

        self.assertEqual(len(game.playersHands["1"]), 13)
        self.assertEqual(len(game.playersHands["2"]), 13)
        self.assertEqual(len(game.playersHands["3"]), 13)
        self.assertEqual(len(game.playersHands["4"]), 13)

    def test_gameInit_ThreePlayers(self):
        gameInfo = GameInfo("test_game", "1234", 3)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")
        gameInfo.addPlayer("3")

        game = Game(gameInfo)

        self.assertTrue("1" in game.order)
        self.assertTrue("2" in game.order)
        self.assertTrue("3" in game.order)

        self.assertTrue("1" in game.playersHands)
        self.assertTrue("2" in game.playersHands)
        self.assertTrue("3" in game.playersHands)

    def test_gameRemoveCardsFromPlayer(self):
        gameInfo = GameInfo("test_game", "1234", 2)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")

        game = Game(gameInfo)
        game.order = ["1", "2"]
        game.currPlayerIndex = 0

        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.TWO, Suit.HEARTS)

        game.playersHands = {
            "1" : [c1],
            "2" : [c2]
        }

        game.__removeCardsFromPlayer__("1", [c1])
        self.assertEqual(len(game.playersHands["1"]), 0)

    def test_gameIterateCurrPlayer_AllPlayersCanMove(self):
        gameInfo = GameInfo("test_game", "1234", 3)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")
        gameInfo.addPlayer("3")

        game = Game(gameInfo)
        game.order = ["1", "2", "3"]
        game.currPlayerIndex = 0

        self.assertEqual(game.currPlayerIndex, 0)

        game.__iteratePlayer__()
        self.assertEqual(game.currPlayerIndex, 1)

        game.__iteratePlayer__()
        self.assertEqual(game.currPlayerIndex, 2)

        game.__iteratePlayer__()
        self.assertEqual(game.currPlayerIndex, 0)

    def test_gameIterateCurrPlayer_SkipOnePlayer(self):
        gameInfo = GameInfo("test_game", "1234", 3)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")
        gameInfo.addPlayer("3")

        game = Game(gameInfo)
        game.order = ["1", "2", "3"]
        game.currPlayerIndex = 0
        game.playersHands["2"] = []

        self.assertEqual(game.currPlayerIndex, 0)

        game.__iteratePlayer__()
        self.assertEqual(game.currPlayerIndex, 2)

        game.__iteratePlayer__()
        self.assertEqual(game.currPlayerIndex, 0)

        game.__iteratePlayer__()
        self.assertEqual(game.currPlayerIndex, 2)

    def test_gameMove_PlayLastMove(self):
        gameInfo = GameInfo("test_game", "1234", 2)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")

        game = Game(gameInfo)
        game.state = GameState.PLAYING
        game.order = ["1", "2"]
        game.currPlayerIndex = 0

        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.TWO, Suit.HEARTS)

        game.playersHands = {
            "1" : [c1],
            "2" : [c2]
        }

        game.move([c1])
        
        self.assertEqual(game.lastMove[0], c1)
        self.assertTrue(game.isGameOver())

    def test_gameMove_PlayFirstMove(self):
        gameInfo = GameInfo("test_game", "1234", 2)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")

        game = Game(gameInfo)
        game.state = GameState.PLAYING
        game.order = ["1", "2"]
        game.currPlayerIndex = 0

        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.TWO, Suit.HEARTS)

        game.playersHands = {
            "1" : [c1],
            "2" : [c2]
        }

        game.move([c1])
        
        self.assertEqual(game.lastMove[0], c1)
        self.assertTrue(game.isGameOver())
        self.assertEqual(game.winOrder, ["1", "2"])

    def test_gameMove_TestTwoMoves(self):
        gameInfo = GameInfo("test_game", "1234", 2)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")

        game = Game(gameInfo)
        game.state = GameState.PLAYING
        game.order = ["1", "2"]
        game.currPlayerIndex = 0

        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.TWO, Suit.HEARTS)
        c3 = Card(CardValue.THREE, Suit.HEARTS)

        game.playersHands = {
            "1" : [c3, c2],
            "2" : [c1]
        }

        game.move([c2])
        game.move([c1])
        
        self.assertEqual(game.lastMove[0], c1)
        self.assertTrue(game.isGameOver())
        self.assertEqual(game.winOrder, ["2", "1"])

    def test_gameMove_TestSkip(self):
        gameInfo = GameInfo("test_game", "1234", 2)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")

        game = Game(gameInfo)
        game.state = GameState.PLAYING
        game.order = ["1", "2"]
        game.currPlayerIndex = 0

        c1 = Card(CardValue.ACE, Suit.HEARTS)
        c2 = Card(CardValue.TWO, Suit.HEARTS)

        game.playersHands = {
            "1" : [c1],
            "2" : [c2]
        }

        game.move([])

        self.assertTrue("1" in game.skip_list)
        self.assertEqual(game.order[game.currPlayerIndex], "2")

    def test_game_TradeCards(self):
        gameInfo = GameInfo("test_game", "1234", 2)
        gameInfo.addPlayer("1")
        gameInfo.addPlayer("2")

        game = Game(gameInfo)

        player1Hand = game.playersHands["1"]
        cardsToTrade = [
            player1Hand[0],
            player1Hand[1]
        ]
        
        self.assertTrue(game.tradeCards("1", cardsToTrade))

        self.assertEqual(len(game.playersHands["1"]), 24)
        self.assertEqual(len(game.playersHands["2"]), 28)
        self.assertTrue(cardsToTrade[0] in game.playersHands["2"])
        self.assertTrue(cardsToTrade[1] in game.playersHands["2"])
        self.assertTrue("1" not in game.trading)
        self.assertTrue("2" in game.trading)

        player2Hand = game.playersHands["2"]
        cardsToTrade = [
            player2Hand[0],
            player2Hand[1]
        ]
        
        self.assertTrue(game.tradeCards("2", cardsToTrade))

        self.assertEqual(len(game.playersHands["1"]), 26)
        self.assertEqual(len(game.playersHands["2"]), 26)
        self.assertTrue(cardsToTrade[0] in game.playersHands["1"])
        self.assertTrue(cardsToTrade[1] in game.playersHands["1"])
        self.assertTrue("1" not in game.trading)
        self.assertTrue("2" not in game.trading)