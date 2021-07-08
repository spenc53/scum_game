from game.player import Player
from server.game_manager import GameManager
from enum import Enum

class CommandDestination(Enum):
    ALL = 1
    GAME = 2
    PLAYER = 3

class BaseClientCommand():
    def __init__(self, commandType: str, commandDestination: CommandDestination, id: str):
        self.dest = commandDestination
        pass

class PlayerJoinGameInfoCommand(BaseClientCommand):
    def __init__(self):
        pass

class PlayerCreatedCommand(BaseClientCommand):
    def __init__(self, p: Player):
        super().__init__("PlayerCreatedCommand", CommandDestination.PLAYER, p.id)
        self.data = p


# it should be formatted as:
'''
{
    CommandDest: ALL / LOBBY / PLAYER,
    Id: '' / GameID / PlayerId
    CommandType: CommandType
}
'''

