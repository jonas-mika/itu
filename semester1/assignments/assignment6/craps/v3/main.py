from subfunctions import *

def play_craps():
    """Simulates a game of Craps"""
    print("Welcome to a Game of Craps!")
    print("----------------------\n")
    print(input("Press 'Enter' to roll the Dice!"))

    result_p1 = phase1()

    if result_p1 not in [True, False]:
        result_p2 = phase2(result_p1)
        return result_p2
    else:
        return result_p1

def main():
    play_craps()

if __name__ == "__main__":
    main()