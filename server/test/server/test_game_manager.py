import unittest

from server.game_manager import GameManager

class TestGameManager(unittest.TestCase):

    def test_AddPlayer(self):
        gameManager = GameManager()

        self.assertEqual(len(gameManager.players), 0)

        p = gameManager.createPlayer("123", "test_player")

        self.assertEqual(len(gameManager.players), 1)
        self.assertEqual(p.id, "123")
        self.assertEqual(p.name, "test_player")

    def test_GetPlayer(self):
        gameManager = GameManager()

        self.assertEqual(len(gameManager.players), 0)

        gameManager.createPlayer("123", "test_player")
        p = gameManager.getPlayer("123")
        
        self.assertEqual(len(gameManager.players), 1)
        self.assertEqual(p.id, "123")
        self.assertEqual(p.name, "test_player")

    def test_DeletePlayer(self):
        gameManager = GameManager()

        self.assertEqual(len(gameManager.players), 0)

        gameManager.createPlayer("123", "test_player")
        p = gameManager.getPlayer("123")
        self.assertIsNotNone(p)
        gameManager.deletePlayer("123")
        self.assertIsNone(gameManager.getPlayer("123"))

    def test_createGameInfo(self):
        gameManager = GameManager()

        p = gameManager.createPlayer("123", "test_player")

        gameInfo = gameManager.createGameInfo(p.id, "456", 4)
        self.assertIsNotNone(gameInfo.id)
        self.assertEqual(gameInfo.name, "456")
        self.assertEqual(len(gameInfo.players), 1)
        self.assertEqual(gameInfo.players[0], p.id)

    def test_getGame(self):
        gameManager = GameManager()

        p = gameManager.createPlayer("123", "test_player")

        gameInfoId = gameManager.createGameInfo(p.id, "456", 4).id

        gameInfo = gameManager.getGameInfo(gameInfoId)

        self.assertIsNotNone(gameInfo.id)
        self.assertEqual(gameInfo.name, "456")
        self.assertEqual(len(gameInfo.players), 1)
        self.assertEqual(gameInfo.players[0], p.id)

    def test_addPlayerToGameInfo(self):
        gameManager = GameManager()

        p = gameManager.createPlayer("123", "test_player")

        gameInfoId = gameManager.createGameInfo(p.id, "456", 4).id

        p2 = gameManager.createPlayer("test_id", "test_player_2")


        gameManager.addPlayerToGameInfo(p2.id, gameInfoId)

        gameInfo = gameManager.getGameInfo(gameInfoId)
        self.assertEqual(len(gameInfo.players), 2)
        self.assertEqual(gameInfo.players[1], p2.id)




