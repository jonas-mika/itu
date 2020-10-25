import random

class Card:

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

def generate_regular_deck():
    for suit in "chsd":
        for rank in range(1,13+1):
            regular_deck = [Card(rank, suit)]
    
    return regular_deck

def shuffle():
    """Return shuffled regular deck"""
    pass

def assign_cards():
    pass

def play_war():
    print(generate_regular_deck)
    # shuffle the deck
    # split the deck randomly into two halfs


play_war()