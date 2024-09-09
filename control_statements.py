# Starting the python project
# This is a guessing game that I use to learn a new language
from random import randint
# random to generate random numbers
from time
from sys, os

def isGuessCorrect(number, secretNumber):
    if (number == secretNumber):
        print("Congratulations! You guessed correctly", secretNumber)
        return True

    if (number < secretNumber):
        print("Guess a little higher to succeed.")
        return False
    elif (number > secretNumber):
        print("Guess a little lower to succeed.")
        return False
    else:
        print("Hooray!, you succeeded. Play again soon")
        return True

    return False


def GuessingGame():
    number = 0
    secretNumber = randint(0, 50) # Generate a random integer between 0-50
    print("Random number has been generated.")
    print('''
           /-------\  
          |         | |  |     |   | |  _______| 
          |  _______  |  |     |   | |  |____    
          |  |    ___ |  |     |   | |  _____|
          |  |___|  | |  |_____|   | |  |______
          |      |  | |            | |         |
           \ ___/|__| |________/|__| |_________|
          ''')
    time.sleep(1)
    print("loading...")
    time.sleep(4)

    os.system("cls")
    print("Welcome to the Guessing Game...")
    while(number != secretNumber):
        number = int(raw_input("Enter a number to guess: "))
        if (number == secretNumber):
            return isGuessCorrect(number, secretNumber)
        elif (number < secretNumber):
            return isGuessCorrect(number, secretNumber)
        elif (number > secretNumber):
            return isGuessCorrect(number, secretNumber)
        else:
            print("Try again soon. Looks like you have no luck today. :-)")


if ("__name__" == __main__):
    # The main entry of the application
    GuessingGame()
