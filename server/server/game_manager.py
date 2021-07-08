import uuid

from game.game import Game
from game.game_info import GameInfo
from game.player import Player

class GameManager():
    instance = None

    def getInstance():
        if GameManager.instance == None:
            GameManager.instance = GameManager()
        return GameManager.instance

    def __init__(self):
        self.games: "dict[str, Game]" = {}
        self.gameInfos: "dict[str, GameInfo]" = {}
        self.players: "dict[str, Player]" = {}

    def createGameInfo(self, playerId: str, name: str, maxPlayers: int) -> GameInfo:
        # include check to see if player exists?

        gameInfo = GameInfo(name, uuid.uuid4(), maxPlayers)
        gameInfo.addPlayer(playerId)
        self.gameInfos[gameInfo.id] = gameInfo
        return gameInfo

    def addPlayerToGameInfo(self, playerId: str, gameInfoId: str):
        # check to see if player exists

        # check to see if game info exists

        # check to see if game is full

        gameInfo = self.gameInfos[gameInfoId]
        gameInfo.addPlayer(playerId)
        pass

    def getGameInfo(self, gameInfoId: str):
        if gameInfoId not in self.gameInfos:
            raise ValueError("Could not find game info")

        return self.gameInfos[gameInfoId]

    def createPlayer(self, id: str, name: str) -> Player:
        p = Player(name, id)
        self.players[id] = p
        return p

    def getPlayer(self, playerId: str) -> Player:
        if not playerId in self.players:
            return None
        return self.players[playerId]

    def playerLeaveGameInfo(self, gameId: str, playerId: str):
        pass

    def deletePlayer(self, playerId: str):
        # remove player from game
        if playerId in self.players:
            del self.players[playerId]