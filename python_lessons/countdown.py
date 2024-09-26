# Count down to 0 from a number given
number = int(input("Please enter a number: "))

count = number

while count <= number and count >= 0:
    if (count in range(0, number)):
        print("Result: ", count)
        count -= 1
