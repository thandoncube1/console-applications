#include <ios>
#include <iostream>
#include <stdio.h>    // printf, scanf, puts, NULL
#include <string>
#include <cstdlib>   // srand(), rand()
#include <time.h>     // time

bool isGuessCorrect(int number, int secretNumber);
int main() {
    std::cout << "This is a sample game for beginnners. \n";

    srand(time(NULL));

    int number = 0;
    int secretNumber = rand() % 100;
    int numberOfguessAllowed = 10;
    int numberOfGuesses = 0;

    // Assign memory
    int* guess = &number; // Pointer
    int& incrementRef = numberOfGuesses; // Reference

    while (secretNumber != *guess && (numberOfGuesses <= numberOfguessAllowed)) {
      if (numberOfGuesses == numberOfguessAllowed) {
        std::cout << "\nYou have reached the max number of guesses\nTry again soon! Enjoy.\n";
        return 0;
      }

      printf("\nCurrent chances remaining: %d\n", (numberOfguessAllowed - incrementRef));
      printf("Guess the number between (1 - 50): ");
      std::cin >>  *guess;
      bool result = isGuessCorrect(*guess, secretNumber);

      if (result == true) {
        std::cout << std::boolalpha << result << "  -  Number: " << secretNumber << "\n";
      }

      if (result == false && *guess < secretNumber) {
        printf("Guess a little higher to succeed. %2d\n", *guess);
      } else if (result == false && *guess > secretNumber) {
        printf("Guess a little lower to succeed. %2d\n", *guess);
      } else {
        std::cout << "Hooray! Thank you for playing. Join us again.\n";
      }
      // Increment Reference
      incrementRef++;
    }

    return 0;
  }

bool isGuessCorrect(int number, int secretNumber) {
  // Check if the number is equal to the secret number
  // Use conditional statements to evaluate

  if (number == secretNumber) {
    return true;
  }

  return false;
}



