# Programming an addition calculator
choice = True or False # Nullish coalescing (True unless you select False)
select = { "No": False, "Yes": True } # Initializing option

while choice != False:
    userIO = int(input("Enter the 1st number: "))
    userIO_2 = int(input("Enter the 2nd number: "))
    print(f"Adding {userIO} and {userIO_2} gives a result of {userIO + userIO_2}")
    option = str(input("Would you like to continue (Yes or No): ")).capitalize()
    if select[option] is not choice:
        print("Thank you for using our program")
        break
