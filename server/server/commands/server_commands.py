from game.player import Player
from game.game import Game
from server.commands.client_commands import BaseClientCommand
from server.game_manager import GameManager
import uuid

from server.commands.client_commands import *

class BaseServerCommand():
    def __init__(self, id: str):
        self.id = id
        self.gameManager = GameManager.getInstance()

    def execute(self) -> "list[BaseClientCommand]":
        raise ValueError("NOT IMPLEMENTED")

class CreateGameCommand(BaseServerCommand):
    def __init__(self, id: str, name: str):
        super().__init__(id)
        self.name = name

    def execute(self) -> "list[BaseClientCommand]":
        player = self.gameManager.getPlayer(self.id)
        self.gameManager.createGame(self.name, player)
        return []

class RegisterPlayerCommand(BaseServerCommand):
    def __init__(self, name):
        super().__init__('')
        self.name = name

    def execute(self) -> 'list[BaseClientCommand]':
        p: Player = self.gameManager.createPlayer(str(uuid.uuid4()), self.name)    
        print(self.gameManager.players) 
        # create command to emit to player
        return [
            PlayerCreatedCommand(p)
        ]