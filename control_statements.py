# Starting the python project
# This is a guessing game that I use to learn a new language
from random import randint
# random to generate random numbers
import time
import sys, os

"""
This is a very simple Guessing Game in Python

 ------------------------------------------
|                                          |
|     Welcome to the Guessing Game         |
|                                          |
 ------------------------------------------

 This is a really good game or starting point to learn the basics of control structures
 and looping in most programming languages. Having the ability to manipulate these 
 Things can help you as a programmer understand what you need to keep excelling in this
 Coding life or journey. Thank you for spending some time to look at my game and if you
 can contribute you are more than welcome to create a `pull request`.
"""

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


def GuessingGame(maxLimit):
    number = 0
    numberOfGuesses = 0
    secretNumber = randint(0, 50) # Generate a random integer between 0-50
    print("Random number has been generated.")

    time.sleep(1)
    print("""

 ------------------------------------------
|                                          |
|     Welcome to the Guessing Game         |
|                                          |
 ------------------------------------------
   """)
    time.sleep(1)
    print("loading...")
    time.sleep(4)

    os.system("clear") # Clear the screen for mac
    print("Welcome to the Guessing Game...")
    while(number != secretNumber and numberOfGuesses <= maxLimit):
        print(f"Chances remaining: {int(maxLimit - numberOfGuesses)+1}")
        number = int(input("Enter a number to guess: "))
        if (numberOfGuesses == maxLimit):
            print(f"""\n--------------------------------------\nRemaining chances: {maxLimit-numberOfGuesses}\nSorry, try again next time.\nMax Limit number of guesses reached.\n--------------------------------------""")
            return False

        if (number == secretNumber):
            isGuessCorrect(number, secretNumber)

        if (number < secretNumber):
            isGuessCorrect(number, secretNumber)
        elif (number > secretNumber):
            isGuessCorrect(number, secretNumber)

        numberOfGuesses += 1

def main():
    print("You are playing the Guessing Game\n")
    input("Press ENTER/RETURN key to continue...")
    time.sleep(2)
    limit = int(input("Enter max limit to start the game: ") or 10)
    GuessingGame(limit)


if (__name__ == '__main__'):
    # The main entry of the application
    main()
