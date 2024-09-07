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

    while (secretNumber != number && (numberOfGuesses < numberOfguessAllowed)) {
      if (numberOfGuesses == numberOfguessAllowed) {
        std::cout << "You reached your limit for this game\nTry again later!\n";
      }

      printf("Guess the number between (1 - 50): ");
      std::cin >>  number;
      bool result = isGuessCorrect(number, secretNumber);

      if (result == true) {
        std::cout << std::boolalpha << result << "  -  Number: " << secretNumber << "\n";
      }

      if (result == false && number < secretNumber) {
        printf("Guess a little higher to succeed. %10d\n", number);
      } else if (result == false && number > secretNumber) {
        printf("Guess a little lower to succeed. %10d\n", number);
      } else {
        std::cout << "Hooray! Thank you for playing. Join us again.\n";
      }

      numberOfGuesses++;
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



