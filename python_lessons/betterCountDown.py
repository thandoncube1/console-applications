# Better count down with time
from time import sleep

print("=="*30)
print("""
        Welcome to the Count Down!! ⏰

        You can select the option you want
        in Seconds (s) or in Minutes (m)
        Select your option below: 
      """)
try:
    select = str(input("Please select your preference (m) or (s):"))
except ValueError:
    print("Wrong input selected, Please enter either (m) or (s)")

if (select.strip().upper() == "m".upper()):
    try:
        timeInput = int(input("Please enter time in minutes: "))
    except ValueError:
        print("Wrong input selected, Please enter time in minutes.")

    minute = timeInput
    second = 0
elif (select.strip().upper() == "s".upper()):
    try:
        timeInput = int(input("Please enter time in seconds: "))
    except ValueError:
        print("Wrong input selected, Please enter time in seconds")

    minute = timeInput // 60
    second = timeInput % 60
    if timeInput < 60:
        second = timeInput
        minute = 0

# Write the loop structures that deal with time
while minute >= 0:
    while second >= 0:
        if (second < 10):
            print(f"Count down in {minute}:{second:02d}")
        else: print(f"Count down in {minute}:{second}")
        second -= 1
        sleep(1)
    minute -= 1
    second = 59

print("Our Rocket has Launched 🚀", end=" ")
print("Thank you for supporting out mission.")



