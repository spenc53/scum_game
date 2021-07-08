import unittest
import uuid

from game.game_info import GameInfo
from game.player import Player

class Test_Game(unittest.TestCase):

    def test_AddPlayersToGame(self):
        g = GameInfo("test_game", "1234", 4)

        p1 = Test_Game.__createPlayer__("player_one")
        p2 = Test_Game.__createPlayer__("player_one")
        p3 = Test_Game.__createPlayer__("player_one")
        p4 = Test_Game.__createPlayer__("player_one")

        g.addPlayer(p1)
        g.addPlayer(p2)
        g.addPlayer(p3)
        g.addPlayer(p4)

        self.assertEqual(len(g.players), 4)
        self.assertEqual(g.players[0], p1)
        self.assertEqual(g.players[1], p2)
        self.assertEqual(g.players[2], p3)
        self.assertEqual(g.players[3], p4)

    def test_AddPlayerTwiceToGame(self):
        g = GameInfo("test_game", "1234", 4)

        p1 = Test_Game.__createPlayer__("player_one")

        g.addPlayer(p1)

        try:
            g.addPlayer(p1)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_AddMoreThanMaxPlayers(self):
        g = GameInfo("test_game", "1234", 2)

        p1 = Test_Game.__createPlayer__("player_one")
        p2 = Test_Game.__createPlayer__("player_two")
        p3 = Test_Game.__createPlayer__("player_three")

        g.addPlayer(p1)
        g.addPlayer(p2)

        try:
            g.addPlayer(p3)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_playerLeave(self):
        g = GameInfo("test_game", "1234", 4)

        p1 = Test_Game.__createPlayer__("player_one")
        p2 = Test_Game.__createPlayer__("player_two")

        g.addPlayer(p1.id)
        g.addPlayer(p2.id)

        self.assertEqual(len(g.players), 2)

        g.playerLeave(p1.id)

        self.assertEqual(len(g.players), 1)
        self.assertEqual(g.players[0], p2.id)

    def test_playerLeaveDoesNotExist(self):
        g = GameInfo("test_game", "1234", 4)

        p1 = Test_Game.__createPlayer__("player_one")
        p2 = Test_Game.__createPlayer__("player_two")

        g.addPlayer(p1)

        self.assertEqual(len(g.players), 1)

        g.playerLeave(p2.id)

        self.assertEqual(len(g.players), 1)
        self.assertEqual(g.players[0], p1)

    def test_playerReadyUp(self):
        g = GameInfo("test_game", "1234", 4)

        p1 = Test_Game.__createPlayer__("player_one")
        p2 = Test_Game.__createPlayer__("player_two")

        g.addPlayer(p1.id)
        g.addPlayer(p2.id)

        self.assertEqual(len(g.players), 2)

        g.playerReadyUp(p1.id)
        self.assertEqual(g.readyPlayers[0], p1.id)
        pass

    def test_PlayerReadyUpThenLeave(self):
        g = GameInfo("test_game", "1234", 4)

        p1 = Test_Game.__createPlayer__("player_one")
        p2 = Test_Game.__createPlayer__("player_two")

        g.addPlayer(p1.id)
        g.addPlayer(p2.id)

        self.assertEqual(len(g.players), 2)

        g.playerReadyUp(p1.id)
        self.assertEqual(g.readyPlayers[0], p1.id)
        pass

    def __createPlayer__(name: str) -> Player:
        return Player(name, uuid.uuid4())
