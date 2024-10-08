#include <iostream>
#include <string>

/*
  Include directly the different
  headers from cppconn/ and mysql_driver.h + mysql_util.h
  (and mysql_connection.h). This will reduce your build time!
*/
#include "mysql_connection.h"

#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>

struct Person {
  std::string firstName;
  std::string lastName;
  int age = 0;
  std::string email;
  std::string picture;
  char gender;
  std::string phoneNumber = 0;
  bool isLibraryStuff = 0;
  bool isActiveMember = 0;
};

class Library {
  private:
    std::string libraryName;
    std::string location;
    std::string openingHours;
    double contactNumber;
  
  public:
    Library() {}
    Library(std::string libraryName, std::string location, std::string openingHours, double contactNumber){
      this->libraryName = libraryName;
      this->location = location;
      this->openingHours = openingHours;
      this->contactNumber = contactNumber;
    }

    ~Library();

    // Create getters and setters for the Library application
    void setLibraryName(std::string libraryName) {
      this->libraryName = libraryName;
    }

    std::string getLibraryName() {
      return this->libraryName;
    }

    void setOpeningHours(std::string openingHours) {
      this->openingHours = openingHours;
    }

    std::string getOpeningHours() {
      return this->openingHours;
    }

    double getContactNumber() {
      return this->contactNumber;
    }



};

int main() {
  std::cout << "Welcome to the Library Application \n";
  return 0;
}
