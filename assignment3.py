# Assignment 3
# Author - Thando Ncube
# Welcome to the Invoice Console Application
print("**"*30)
print(" "*15)
print("Welcome to the Invoice Console Application")
print(" "*15)
print("**"*30)
# Initialize the tax value
HST = 0.13
# initializing statement
isActive = True
# Initialize the list for purchases
listOfInvoices = list()

while isActive != False:
    # Get all the values of the variable inputs
    clientName = input("Please enter the Company name: ")
    consultant = input("Please enter consultant name: ")
    hourlyRate = float(input("Please enter the hourly rate: "))
    hoursWorked = int(input("Please enter the hours worked: "))
    subTotal = hourlyRate * hoursWorked
    tax = subTotal * HST
    total = subTotal + tax
    # Assign each variable to a key in the clientInvoice object
    clientInvoice = { 
        "clientName": clientName, 
        "consultant": consultant, 
        "hourlyRate": hourlyRate, 
        "hoursWorked": hoursWorked, 
        "subTotal": subTotal, 
        "tax": tax, 
        "total": total 
    }
    # push each client invoice into the list
    listOfInvoices.append(clientInvoice)
    option = str(input("Would you like to continue (Y) or (N): ")).capitalize()
    if option == "N":
        print("Option is equal to N")
        break


# Print all invoices
print("--"*30)
print(" "*15)
print("Invoice for Consultants")
print(" "*15)
print("--"*30)
for invoice in listOfInvoices:
    # Iterate over each item in the list of invoices
    print("|",end=" {}".format(invoice.get("clientName")))
    print("|",end=" Consultant: {} \n".format(invoice.get("consultant")))
    print("|",end=" Hours worked: {} \n".format(invoice.get("hoursWorked")))
    print("|",end=" Subtotal: ${subTotal:.2f} \n".format(subTotal=invoice.get("subTotal")))
    print("|",end=" HST: ${tax:.2f} \n".format(tax=invoice.get("tax")))
    print("|",end=" Total: ${total:.2f} \n".format(total=invoice.get("total")))
    print("--"*30)