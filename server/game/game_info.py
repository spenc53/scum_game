from game.card import Card
from game.deck import Deck
from game.player import Player

class GameInfo():
    def __init__(self, name: str, id: str, maxPlayers: int):
        """Game constructor

        Args:
            name (str): Title of the game
            id (str): Id of the game
            maxPlayers (int): Max Players to have in the Game
        """
        self.maxPlayers = maxPlayers
        self.players: "list[str]" = []
        self.readyPlayers: "list[str]" = []
        self.name = name
        self.id = id

        self.currMove = ""

    def addPlayer(self, playerId: str):
        """Add a player to the game

        Args:
            player (Player): Player to add to the game

        Raises:
            ValueError: Too many players
            ValueError: Player already in the game
        """        
        if len(self.players) >= self.maxPlayers:
            raise ValueError("Max players reached for game")

        if playerId in self.players:
            raise ValueError("Player already in game")

        self.players.append(playerId)

    def playerLeave(self, playerId: str):
        """Remove a player from the game. If the player is not in the game nothing is done

        Args:
            playerId (str): The id of the player to remove
        """        
        self.playerUnReadyUp(playerId)
        
        if playerId in self.players:
            self.players.remove(playerId)

    def playerReadyUp(self, playerId: str):
        """Adds player to ready list. If player is not in game, nothing is done

        Args:
            playerId (str): player to put in ready list
        """        

        # Check to make sure player is in this game
        if playerId not in self.players:
            return

        # add player to ready list
        if playerId not in self.readyPlayers:
            self.readyPlayers.append(playerId)

    def playerUnReadyUp(self, playerId: str):
        """Removes a player from a ready state. If player is not in the ready list, nothing is done.

        Args:
            playerId (str): PlayerId of the player to remove from the ready list
        """
        # remove player from ready player list
        if playerId in self.readyPlayers:
            self.readyPlayers.remove(playerId)

    