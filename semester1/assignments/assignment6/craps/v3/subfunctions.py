from helpers import *

def phase1():
    roll1, sum1 = dice_roll()

    print("Come-Out Roll: {}".format(roll1))
    print("Come-Out Sum: {}".format(sum1))
    print("--------------")

    if sum1 in [7,11]:
        return game_win()
    elif sum1 in [2,3,12]:
        return game_loss()
    else:
        print("Continue Playing! ...\n")
        return sum1

def phase2(sum1):    
    while True:
        print(input("Roll the Dice again by pressing 'Enter'"))
        next_roll, next_sum = dice_roll()

        print("Roll Phase 2: {}".format(next_roll))
        print("Sum Phase 2: {}".format(next_sum))
        print("--------------")

        if next_sum == sum1:
            return game_win()
        elif next_sum == 7:
            return game_loss()