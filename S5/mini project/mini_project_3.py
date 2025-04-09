import time
from os import system, name
while True:
    choise = input("Do you want to start? (y/n)")
    if 'y' in choise.lower():
        h = int(input("Enter Amount of hour: "))
        m = int(input("Enter Amount of minutes: "))
        s = int(input("Enter Amount of seconds: "))
        total = h * 3600 + m * 60 + s
        print("Time start now...")
        time.sleep(1)
        while total >= 1:
            print(total)
            total -= 1
            time.sleep(1)
            if name == "nt":
                system("cls")
            else:
                system("clear")
        print("Time Ended...")
    elif 'n' in choise.lower():
        print("*** See you later! ***")
        break 
    else:
        print("Invalid input....")