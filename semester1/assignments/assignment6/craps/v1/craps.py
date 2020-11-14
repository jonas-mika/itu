import random


def two_dice_roll():
    """Simulates a random roll of two dices and return the result in a list of integers"""
    return [random.randint(1,6), random.randint(1,6)]

def get_sum(L):
    """Returns the sum of two dices rolled"""
    return sum(L)

def craps():
    """Simulates a game of Craps"""
    gameOver = False 
    roll1 = two_dice_roll()
    sum_roll1 = get_sum(roll1)

    while gameOver is False:
        if sum_roll1 in [7,11]: 
            game_result = True
            gameOver = True
        
        elif sum_roll1 in [2,3,12]:
            game_result = False
            gameOver = True 
        
        else:
            while gameOver is False: 
                next_roll = two_dice_roll()
                sum_next_roll = get_sum(next_roll)

                if sum_next_roll == sum_roll1:
                    game_result = True
                    gameOver = True
                
                elif sum_next_roll == 7:
                    game_result = False
                    gameOver = True
            
    return game_result

print(craps())