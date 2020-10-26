# Contains Classes used for the Game War

class Card:
    """ A class representing a card from a standard card deck """

    def __init__(self, rank, suit):
        assert type(rank) == int, "Please insert the Data Type Integer as a Rank"
        assert 1 <= rank <= 13, "The Rank needs to be within the range 1-13"
        self.rank = rank        
        
        assert type(suit) == str, "Please insert the Data Type String for the Suit"
        assert suit in ["d", "c", "h", "s"]
        self.suit = suit

    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def value(self):
        if self.rank == 1:
            value = 1
        elif self.rank  >= 10:
            value = 10
        else: 
            value = self.rank 
        
        return value

    def __str__(self):
        suits = {
            "d": "Diamonds", 
            "c": "Clubs", 
            "h": "Hearts", 
            "s": "Spades"
            }
            
        faces = {
            1: "Ace",
            2: "Two",
            3: "Three", 
            4: "Four",
            5: "Five", 
            6: "Six",
            7: "Seven",
            8: "Eight", 
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12 :"Queen", 
            13: "King", 
            }

        return "{} of {}".format(faces[self.rank], suits[self.suit])

class Player:
    """ A Class representing a Player in a game of War """

    def __init__(self):
        pass

    def getCards(self):
        pass