# Main Script to run the War Game

from helpers import generate_regular_deck, shuffle, assign_cards
from classes import * 
import random

def main():
    regular_deck = generate_regular_deck()

    shuffle(regular_deck)

    print("Both Players received equally many cards")
    cards_playerA, cards_playerB = assign_cards(regular_deck)

    i = 0
    
    while len(cards_playerA) not in [0,52] and i<1000:
        print(f"Card Rank of Player A: {cards_playerA[0].rank}")
        print(f"Card Rank of Player B: {cards_playerB[0].rank}")
        if cards_playerA[0].rank > cards_playerB[0].rank:
            print("Card of A won.")
            cards_playerA.append(cards_playerB.pop(0))
            cards_playerA.append(cards_playerA.pop(0))
            print(f"Number of A is now: {len(cards_playerA)}")
            print(f"Number of B is now: {len(cards_playerB)}")
        elif cards_playerA[0].rank < cards_playerB[0].rank:
            print("Card of B won.")
            cards_playerB.append(cards_playerB.pop(0))
            cards_playerB.append(cards_playerA.pop(0))
            print(f"Number of A is now: {len(cards_playerA)}")
            print(f"Number of B is now: {len(cards_playerB)}")
        else:
            print("It is war!!! Both Players reveal two more cards")
            if cards_playerA[2].rank > cards_playerB[2].rank:
                print("Player A has won the War.")
                for i in range(3):
                    cards_playerA.append(cards_playerB.pop(0))
                    cards_playerA.append(cards_playerA.pop(0))
                print(f"Number of A is now: {len(cards_playerA)}")
                print(f"Number of B is now: {len(cards_playerB)}")
            else:
                print("Player B has won the war.")
                for i in range(3):
                    cards_playerB.append(cards_playerB.pop(0))
                    cards_playerB.append(cards_playerA.pop(0))
                print(f"Number of A is now: {len(cards_playerA)}")
                print(f"Number of B is now: {len(cards_playerB)}")
        i+=1
    print("-------------------")
    print("SUMMARY")
    print("The game has ended.")
    if len(cards_playerA) == 0:
        print("Player B won.")
    elif len(cards_playerA) == 52:
        print("Player A won.")
    else:
        print(f"The game was stopped at {i} interations.")
        if len(cards_playerA) > len(cards_playerB):
            print(f"Player A has won these {i} rounds.")
        elif len(cards_playerA) < len(cards_playerB):
            print(f"Player B has won these {i} rounds.")
        else:
            print("It was a tie.")
    print(f"The game lasted {i} rounds")

main()