import random

def dice_roll():
    """Simulates a random roll of two dices and return the result in a list of integers"""
    dice_roll = [random.randint(1,6), random.randint(1,6)]
    return (dice_roll, sum(dice_roll))


def game_win():
    """Actions executed, when the Player won the game"""
    print("You won!")
    return True

def game_loss():
    """Actions executed, when the Player lost"""
    print("You lost!")
    return False