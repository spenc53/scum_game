from game.card import Card

class Player():
    def __init__(self, name: str, id: str):
        """Create a new player

        Args:
            name (str): Name of the player
            id (str): Id of the player
        """
        self.name = name
        self.id = id
