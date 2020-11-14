# Contains helper functions for main for game of war

from classes import Card
import random

def generate_regular_deck():
    """ Generates a regular set of 52 cards represented as a list of Card objects """
    
    print("A regular Deck of 52 Cards was created.")
    return [Card(rank, suit) for suit in "chsd" for rank in range(1,13+1)]

def shuffle(deck):
    """ Shuffles a regular deck """

    print("The deck was shuffled.")
    return random.shuffle(deck) # shuffles a list

def assign_cards(deck):
    """ Splits the Deck into two evenly big (26) stacks of cards represented as a list of list of Card objects """

    return [deck[:int(len(deck)/2)], deck[int(len(deck)/2):]]