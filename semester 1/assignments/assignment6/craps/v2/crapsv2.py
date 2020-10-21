import random

def two_dice_roll():
    """Simulates a random roll of two dices and return the result in a list of integers"""
    return [random.randint(1,6), random.randint(1,6)]

def get_sum(L):
    """Returns the sum of two dices rolled"""
    return sum(L)

def game_win():
    print("You won!")
    return 1, _

def game_loss():    
    print("You loose!")
    return 0, _

def phase1():
    roll1 = two_dice_roll()
    sum1 = get_sum(roll1)

    print("Come-Out Roll: {}".format(roll1))
    print("Come-Out Sum: {}".format(sum1))
    print("--------------")

    if sum1 in [7,11]:
        return game_win()
    elif sum1 in [2,3,12]:
        return game_loss()
    else:
        print("Continue Playing! ...\n")
        return -1, sum1

def phase2(sum1):    
    while True:
        print(input("Roll the Dice again by pressing 'Enter'"))
        next_roll = two_dice_roll()
        next_sum = get_sum(next_roll)

        print("Roll Phase 2: {}".format(next_roll))
        print("Sum Phase 2: {}".format(next_sum))
        print("--------------")

        if next_sum == sum1:
            return game_win()
        elif next_sum == 7:
            return game_loss()

def craps():
    """Simulates a game of Craps"""
    print("Welcome to a Game of Craps!")
    print("----------------------\n")
    print(input("Press 'Enter' to roll the Dice!"))

    result_p1, sum1 = phase1()

    if result_p1 == -1:
        result_p2, _ = phase2(sum1)
        return bool(result_p2)
    else:
        return bool(result_p1)

if __name__ == "__main__":
    craps()