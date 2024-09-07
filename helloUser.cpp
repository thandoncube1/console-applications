#include <iostream>
#include <string>
#include <ctime>
#include <stdio.h>

int getAge(int age);
int main() {
    std::cout << "Welcome! Please enter your name: ";
    std::string name;
    std::cin >> name;
    // Able to add  numbers to my vim setup
    // More comments to work with
    int userAge = 0;
    std::cout << "Enter your age: ";
    std::cin >> userAge;
    // This is a comment string from my last program
    std::cout << "Hello and Welcome " << name << "\n";
    std::cout << "Get the year when " << name << " was born: " << getAge(userAge) << "\n";
    
    printf("Age: %d", userAge);

    return 0;
}

int getAge(int age) {
  std::time_t time = std::time(nullptr);
  std::tm *const pTInfo = std::localtime(&time);

  int year = 1900 + pTInfo->tm_year;
  int result = year - age;
  return result;
}
