import random
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "~!@#$%^&*()_+-|/><?"
numbers = "0123456789"
all = lower + upper + symbols + numbers

while True:
    print("choise one of the options: \n\t 1) Crate password \n\t 2) Exit")
    choise = input("Enter option: ")
    if choise == "1":
        length = int(input("Enter the length of password: "))
        password = "".join((random.sample(all, length)))
        print(password)
    if choise == "2":
        print("*** See you later! ***")
        break
    else:
        print("Your choise is Wrong! ")