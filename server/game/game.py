from enum import Enum

from game.game_info import GameInfo
from game.deck import Deck
from game.card import Card
from game.utils.game_util import GameUtil

TRADING_MAP = {
    6: [2, 1, 0, 0, 1, 2],
    5: [2, 1, 0, 1, 2],
    4: [2, 1, 1, 2],
    3: [2, 0, 2],
    2: [2, 2]
}

class Game():
    def __init__(self, gameInfo: GameInfo):
        """Creates a new game from the GameInfo

        Args:
            gameInfo (GameInfo): The GameInfo to make a game from
        """        
        self.gameInfo = gameInfo

        self.playersHands: "dict[str, list[Card]]" = {}
        self.order: "list[str]" = []
        self.currPlayerIndex = 0
        self.lastMove: "list[Card]" = []
        self.winOrder: "list[str]" = []
        self.state: GameState = GameState.SETUP
        self.trading = {}
        self.skip_list = []

        for p in gameInfo.players:
            self.order.append(p)
            self.playersHands[p] = []

        trades = TRADING_MAP[len(self.order)]
        for i in range(0, len(self.order) // 2):
            p1 = self.order[i]
            p2 = self.order[-1 - i]
            self.trading[p1] = {
                "dstPlayer": p2,
                "amount": trades[i],
                "tradeValue": TradingValue.ANY
            }
            self.trading[p2] = {
                "dstPlayer": p1,
                "amount": trades[-1 - i],
                "tradeValue": TradingValue.BEST
            }
            pass

        deck = Deck()
        deck.shuffle()

        # distribute cards
        i = 0
        totalPlayers = len(self.order)
        while not deck.isEmpty():
            currPlayer = self.order[i]
            self.playersHands[currPlayer].append(deck.drawCard())
            i += 1
            i %= totalPlayers

    def resetMatch(self):
        # restart the match with an updated order based on how people won
        pass

    def tradeCards(self, srcPlayerId: str, srcCards: "list[Card]") -> bool:
        if not GameUtil.playerHasCards(self.playersHands[srcPlayerId], srcCards):
            return False
        
        dstPlayerId = self.trading[srcPlayerId]["dstPlayer"]
        del self.trading[srcPlayerId]
        self.__removeCardsFromPlayer__(srcPlayerId, srcCards)
        for c in srcCards:
            self.playersHands[dstPlayerId].append(c)

        return True

    def move(self, move: "list[Card]") -> bool:
        """Play a move for a given player

        Args:
            playerId (str): [description]
            move (list[Card]): [description]

        Returns:
            bool: [description]
        """        
        playerId = self.order[self.currPlayerIndex]
        
        if len(move) == 0:
            self.skip_list.append(playerId)
            self.__iteratePlayer__()
            return True

        if not GameUtil.isValidMove(self.playersHands[playerId], move, self.lastMove):
            return False
        
        # remove card from player hand
        self.lastMove = move
        self.__removeCardsFromPlayer__(playerId, move)
        self.__iteratePlayer__()

        playerHand = self.playersHands[playerId]
        if len(playerHand) == 0:
            self.winOrder.append(playerId)

        self.updateState()

        if self.state == GameState.GAME_OVER:
            for id in self.order:
                if id not in self.winOrder:
                    self.winOrder.append(id)

    def isGameOver(self) -> bool:
        """Get's game over status

        Returns:
            bool: True if the game is over, false otherwise
        """        
        return GameState.GAME_OVER == self.state

    def updateState(self):
        """Updates the state of the game
        """
        if self.state == GameState.SETUP:
            self.state = GameState.NEW_ROUND
            return

        if self.state == GameState.NEW_ROUND:
            self.state = GameState.PLAYING
            return

        i = 0
        for _ in range(len(self.order)):
            self.currPlayerIndex += 1
            self.currPlayerIndex %= len(self.order)

            if len(self.playersHands[self.order[self.currPlayerIndex]]) > 0:
                i += 1

        self.state = GameState.GAME_OVER if i <= 1 else GameState.PLAYING

    def __removeCardsFromPlayer__(self, playerId: str, cards: "list[Card]"):
        """Removes the cards from a players hand

        Args:
            playerId (str): The id of the player to remove cards from
            cards (list[Card]): the cards to remove from the players hand
        """        
        for c in cards:
            self.playersHands[playerId].remove(c)

    def __iteratePlayer__(self):
        """iterates the currPLayerindex
        """        
        for _ in range(len(self.order)):
            self.currPlayerIndex += 1
            self.currPlayerIndex %= len(self.order)

            nextPlayerId = self.order[self.currPlayerIndex]

            if nextPlayerId in self.skip_list:
                continue

            if len(self.playersHands[nextPlayerId]) > 0:
                return

class TradingValue(Enum):
    ANY = 1,
    BEST = 2

class GameState(Enum):
    SETUP = 1,
    NEW_ROUND = 2,
    PLAYING = 3,
    GAME_OVER = 4

# Should we make a hand class, it would just be a collection of cards
class Hand():
    pass
