#This is a sandbox to experiment with Python code
from random import randrange

def D6():
    RollD6 = randrange(6)
    print(RollD6)

def D10():
    RollD10 = randrange(10)
    print(RollD10)

def D20():
    RollD20 = randrange(20)
    print(RollD20)

def main():
    Prompt = input('Would you like to roll a dice? Y/N: ')
    if Prompt == "Y":
        Dice = input('Type "D6" to roll a 6 sided die, "D10" to roll a 10 sided die, or "D20" to roll a 20 sided die ')
        if Dice == "D6":
            D6()
        elif Dice == "D10":
            D10()
        elif Dice == "D20":
            D20()
    else:
        print('No problem, come again another time.')

if __name__ == "__main__":
    main()
