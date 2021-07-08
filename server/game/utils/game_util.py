from game.card import Card
from game.player import Player

class GameUtil():

    def isValidMove(playerHand: "list[Card]", move: "list[Card]", lastMove: "list[Card]") -> bool:
        """Checks if a given move is valid

        Args:
            player (Player): The hand of the player making the move
            move (list[Card]): The move that player wants to make
            lastMove (list[Card]): The move that was last made in the game

        Returns:
            bool: returns true if the move is valid
        """        
        # must make a move, if no move, return false
        if len(move) == 0:
            return False

        if not GameUtil.playerHasCards(playerHand, move):
            return False
        
        if not GameUtil.moveIsAllSameTypeOfCard(move):
            return False

        # if there is no last move, all moves are valid
        if lastMove == None or len(lastMove) == 0:
            return True
        
        if len(lastMove) > len(move):
            # if the last move has more cards, then return false
            return False
        elif len(move) > len(lastMove):
            # check if move is better than last move
            return True
        else:
            # both have same amount of cards, check who has greater value
            return move[0] > lastMove[0]
    
    def playerHasCards(playerHand: "list[Card]", move: "list[Card]") -> bool:
        """Check to see if the player has the cards for the given move

        Args:
            player (Player): The player's hand to check
            move (list[Card]): The move or cards to check to see if the player has

        Returns:
            bool: returns true if player has the cards, false otherwise
        """        
        # check player hand for cards, if player does not have cards, return false
        for c in move:
            if c not in playerHand:
                return False

        return True

    def moveIsAllSameTypeOfCard(move: "list[Card]") -> bool:
        """Check to see if all the cards in the move are of the same value

        Args:
            move (list[Card]): The cards to check if they have the same card value

        Returns:
            bool: returns true if all cards are the same value
        """        
        c1 = move[0]
        for c in move:
            if c.number != c1.number:
                return False
        return True