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
    timeInput = int(input("Please enter time in minutes: "))
elif (select.strip().upper() == "s".upper()):
    timeInput = int(input("Please enter time in seconds: "))
    minute = timeInput // 60
    second = timeInput % 60
    if timeInput < 60:
        second = timeInput
        minute = 0




